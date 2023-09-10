
import warnings
warnings.simplefilter(action='ignore')
import os, sys, time, traceback,copy, gc, shutil,json,traceback,json
from typing import Any, Callable, Sequence, Dict, List , Union
from copy import deepcopy
from box import Box

import fire, pandas as pd, numpy as np


from utilmy import (date_now)



def pd_add_rolling_window_sum(df, colsgroupby=None, colsum='n_clk', window=30, cfg=None, mode='train',
                                  window_shift=1, colnew='sum1')->pd.DataFrame:
    """
    Return ['ymd', 'hh', 'fe', 'n_clk_per_fe_hour_past_30days']
    colsgroupby= ['fe', 'hh' ]

    """
    colsgroupby = [  'fe', 'hh'] if colsgroupby is None else colsgroupby

    if colnew in df.columns :
       log(f"{colnew} already exists, skipping")
       return df

    #### Generate All missing dates as Reference: Need to add MORE dates for 1st dates !!!
    ### datetime format is needed
    t0 = date_now(df['ymd'].min(), fmt_input="%Y%m%d", fmt="%Y-%m-%d", add_days=-window)
    t1 = date_now(df['ymd'].max(), fmt_input="%Y%m%d", fmt="%Y-%m-%d")
    dfh0        = pd.DataFrame({ 'ymd' : [ date_now(x, fmt="%Y%m%d", returnval='int') for x in pd.date_range(t0, t1, freq='D') ] } )
    dfh0['ymd'] = dfh0['ymd'].apply(lambda x : date_now(x, fmt_input="%Y%m%d", returnval='datetime'))
 
    #### Format as datetime
    df = df.sort_values(colsgroupby)
    df['ymd'] = df['ymd'].apply(lambda x : date_now(x, fmt_input="%Y%m%d", returnval='datetime'))


    df2 = pd.DataFrame()
    for kk, (keys, dfh) in enumerate(df.groupby(colsgroupby)):
        # log(kk, keys, len(dfh))
        if len(dfh) <= 1 :    
            dfh[colnew] = 0.0   ## single row : no past data
            df2  = pd.concat((df2, dfh)) 
            continue ### need 2 dates

        ### Create full dates dataframe, zero for missing dates.        
        dfi = dfh0.merge(dfh[[ 'ymd', colsum ]], on='ymd', how='left') 
        dfi[colsum] = dfi[colsum].fillna(0.0)

        ### 30 days rolling single column
        dfi = dfi.set_index('ymd')[colsum].rolling(window).sum().shift(window_shift).reset_index()
        dfi.columns = ['ymd', colnew ] 
        dfi = dfi[dfi[colnew].notna()]
        dfi = dfi[dfi[colnew] >  0 ]   ### zero are not needed

        ### Merge back to original dates
        dfh2 = dfh.merge( dfi, on= ['ymd', ], how='left') 
        df2  = pd.concat((df2, dfh2)) 
        if kk % 10000 == 0 : 
           log(df2.shape, keys)
        # log(dfi)         
        # log(kk,  keys, dfh2) 
        # if kk >= 17: break

    df2[colnew] = df2[colnew].fillna(0.0) 
    df2['ymd']  = df2['ymd'].apply(lambda x : date_now(x, fmt="%Y%m%d", returnval='int'))
    df2 = df2.sort_values(  [ci for ci in colsgroupby if ci not in {'hh'}] +   [ 'hh', 'ymd'])
    return df2





def feat_groupby(dfe, colg, groupby=1, ip=0, fe=1)->pd.DataFrame:
    """ Generate GroupBy Feature Engineering
    """
    dd={'qkey' :   'nunique',}
    if fe>0 : dd['fe'] = 'nunique'
    if ip>0 : dd['ip'] = 'nunique'

    if groupby > 0 :
        dfg = dfe.groupby(colg).agg(dd).reset_index()

    if    len(dd) ==3:  dfg.columns = [ colg,  'n_fe',   'n_quad', 'n_user'  ]
    elif  ip==0       : dfg.columns = [ colg,  'n_fe',   'n_quad',  ]
    elif  fe==0:        dfg.columns = [ colg,  'n_quad', 'n_user'  ]
    else :
        dfg = dfe[[colg]].drop_duplicates()


    dfg1 =  dfe[dfe.y == 1].groupby(colg).agg({ 'scale': 'count'
      }).reset_index()
    dfg1.columns = [colg, 'n_clk']
    dfg =  dfg.merge(dfg1, on=colg, how='left')
    dfg['n_clk']= dfg['n_clk'].fillna(0.0)


    dfg2 =  dfe[dfe.y == 0].groupby(colg).agg({ 'scale': 'count'
      }).reset_index()
    dfg2.columns = [colg, 'n_imp']
    dfg =  dfg.merge(dfg2, on=colg, how='left')
    dfg['n_imp']= dfg['n_imp'].fillna(1.0)

    #### NA Filling
    dfg['ctr'] = dfg['n_clk'] / dfg['n_imp']
    dfg['ctr'] = dfg['ctr'].fillna(  dfg['ctr'].mean() )
    dfg['n_imp'] = dfg.apply(lambda x :  x['n_clk'] / x['ctr'] if  'na' in str(x['n_imp']) else x['n_imp']  , axis=1 )

    return dfg


def pd_groupby(df2, colskey, aggdict, colsfinal=None):
    ### pd_groupby(df2,  [colg], {'fe': 'nunique', },   [ colg,  'n_fe'   ]   )
    df2  = df2.groupby(colskey).agg(aggdict).reset_index()
    df2.columns = colsfinal
    return df2


def featgroup_add_date(df:pd.DataFrame, cols=None, cfg:Dict=None,
                       use_existing_date=True,
                       mode='train')->pd.DataFrame:
    """

    """
    cols  = list(df.columns) if cols is None else cols

    if use_existing_date  :
        df['dt'] = df.apply(lambda x : date_fun_create_dtime_ymdh(x['ymd'], x['hh']), axis=1)

    else :
        dtnow = date_now( fmt='%Y-%m-%d %H:%M:%S', returnval='datetime', timezone='UTC')
        ymd   = date_now( fmt='%Y%m%d',            returnval='int', timezone='UTC')
        hms   = date_now( fmt='%H%M%S',            returnval='int', timezone='UTC')

        df['dt']  = dtnow
        df['ymd'] = float(ymd)
        df['hms'] = hms
        log('Using this date', dtnow)


    colsfeat = [ 'month', 'day', 'hour', 'weekday',   ]

    dftime, coltime =  date_pd_addfeatures(df[['dt']].drop_duplicates("dt"), coldate=['dt'], pars= {'col_add': colsfeat})
    dftime = dftime.drop_duplicates("dt")
    log('features date:', dftime.columns)

    cols0 = [ ci for ci in df.columns if ci not in dftime.columns  ] + [ 'dt' ]  ### Delete previous ones
    df    = df[cols0].merge(dftime[[  ci for ci in dftime.columns  ] ], on=['dt'], how='left')
    cols2 = df.columns
    #df[[ 'dt', 'dt_hour', 'dt_day' ]]

    ### Add ons
    if 'dt-hour' in cols2 :    df['dt-islunch']   = df['dt-hour'].apply(lambda x :     1 if x>= 12 and x < 14 else 0 )
    if 'dt-hour' in cols2 :    df['dt-isevening'] = df['dt-hour'].apply(lambda x :     1 if x>= 18 else 0 )
    if 'dt-weekday' in cols2 : df['dt-isweekend'] = df['dt-weekday'].apply(lambda x :  1 if x in {5,6} else 0 )

    log( sum( dftime['dt-day'].isna() ) )
    # pd_to_file_s3(dftime, dirfeat +"/model/dftime_all.parquet")
    #log_pd(df)
    return df
