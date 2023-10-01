# -*- coding: utf-8 -*-
""" Model template



"""
import os, pandas as pd, numpy as np, scipy as sci
import json, fire, sklearn, joblib
from copy import deepcopy 

from sklearn.linear_model import *
#from sklearn.svm import *
from sklearn.ensemble import *
#from sklearn.tree import *
from lightgbm import LGBMModel, LGBMRegressor, LGBMClassifier, LGBMRanker

####################################################################################################
# from src.utils.utilmy_log import log, log2 

from utilmy import pd_read_file, pd_to_file, log, log2


####################################################################################################
global model, session

def init(*kw, **kwargs):
    global model, session
    model   = Model(*kw, **kwargs)
    session = None

def reset():
    global model, session
    model, session = None, None


####################################################################################################
def test1():
    """
        ['_check_n_features', '_get_param_names', '_get_tags', '_more_tags', '_repr_html_', '_repr_html_inner',
        _repr_mimebundle_', '_validate_data', 'categorical_features', 'display_types', 'features_todrop',
        'final_training_columns', 'fit', 'fit_transform', 'get_params', 'id_columns', 'learned_dtypes',
        'ml_usecase', 'numerical_features', 'response', 'set_params', 'target', 'time_features', 'transform']


    :return:
    """
    global model, session
    dirin="ztmp/local/models/0_Extra/"

    ### model
    load_model(dirin)
    pipe1 = model.model[0]

    method_list = [method for method in dir(pipe1) if method.startswith('__') is False]
    log(method_list)
    log(pipe1.final_training_columns)
    colsX1 = pipe1.final_training_columns

    colsX = pd_read_file(dirin + "/colsX*")
    colsX = list(colsX.columns)
    colsX = [  ci for ci in colsX if 'Unna' not in ci ]

    dfX   = pd_read_file(dirin + "/data/dfs*.parquet", nrows=10)
    dfX = dfX.iloc[:100, :]

    # pd_to_file(dfX, dirin +"/data/dfsample.parquet")

    log('cols used', dfX.columns)

    # dfY = predict(dfX)
    # assert len(dfX[colsX])>0
    colsX2 = ['quadkey', 'fe'  ]
    dfY = predict_proba(dfX[colsX1], merge_proba=True)


    log(dfY)



####################################################################################################
class Model(object):
    def __init__(self, model_pars=None, data_pars=None, compute_pars=None):
        self.model_pars   = model_pars   if  model_pars  is not None else {}
        self.compute_pars = compute_pars if  compute_pars is not None else {}
        self.data_pars    = data_pars    if  data_pars    is not None else {}
        self.info = {}

        ### Proba Model
        self.ythresh = 0.5  
        self.alpha   = 1.0               
        self.model   = None
        self.prepro  = None   

        if model_pars is not None:
            try :
               self.ythresh = model_pars.get('ythresh',  0.5)         
               self.alpha   = model_pars.get('alpha',    1.0)         
               
               model_class = globals()[model_pars['model_class']]
               self.model  = model_class(**model_pars['model_pars'])
               log2(model_class, self.model)
               
            except Exception as e: 
               log(e)
               self.model  = None


def fit(Xtrain=None, ytrain=None, data_pars=None,  Xtest=None, ytest=None, 
        Xtrain_rankgroup=None, Xtest_rankgroup=None, ### Specific for LTR
        compute_pars=None, out_pars=None, use_prepro=False, ww=None, **kw):
    """
    """
    global model, session
    compute_pars = {} if compute_pars is None else compute_pars
    
    if Xtrain is None :
        Xtrain, ytrain, Xtest, ytest = get_dataset(data_pars, task_type="train")

    if use_prepro and model.prepro is not None:        
        Xtrain = model.prepro.transforms(Xtrain)
        Xtest  = model.prepro.transforms(Xtest)
        log('fit:prepro done:', Xtrain.shape)

    log('Data Train shape: ', Xtrain.shape, Xtest.shape)

    if "LGBMClassifier" in model.model_pars['model_class']:
        # assert Xtest is None, log('Xtest is None')
        model.model.fit(Xtrain, ytrain, 
                          eval_set    = [(Xtest, ytest)], 
                          eval_metric = model.model_pars.get('eval_metric', 'logloss' ) ,
                          early_stopping_rounds= model.model_pars.get('early_stopping_rounds',   5),
                          sample_weight= ww,
                          **compute_pars.get("compute_pars", {}))

    elif "LGBMRanker" in model.model_pars['model_class']:
        #model = LGBMRanker(objective="lambdarank",n_estimators=20)
        model.model.fit(Xtrain, ytrain, group=Xtrain_rankgroup, 
                  eval_set   = [(Xtest, ytest)], 
                  eval_group = [Xtest_rankgroup], ### 1D vector: 12,20 : length of ranking list
                  eval_metric= model.model_pars.get('eval_metric', 'map' ),
                  sample_weight= ww)

    else:
        model.model.fit(Xtrain, ytrain, **compute_pars.get("compute_pars", {}))



def predict(Xpred=None, data_pars={}, compute_pars={}, out_pars={},  use_prepro=False, output_binary=False, **kw):
    global model, session

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro : 
        Xpred = model.prepro.transform(Xpred)
        log('predict_proba:Prepro Done:', Xpred.shape)
 
    ythresh     = model.ythresh
    yscore      = model.model.predict(Xpred)
    ypred_proba = 1 / (1 + np.exp(-model.alpha * yscore))
    ypred       = np.array([ 1 if p > ythresh else 0 for p in ypred_proba])
    
    return ypred



def predict_all(Xpred=None, data_pars={}, compute_pars={}, out_pars={}, merge_proba=True, ythresh=0.5, use_prepro=False, **kw):
    global model, session

    if model.prepro is not None : 
        Xpred = model.prepro.transform(Xpred)

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro : 
        Xpred = model.prepro.transform(Xpred)
        log('predict_proba:Prepro Done:', Xpred.shape)

    
    if "LGBMRanker" in model.model_pars['model_class']:
        ythresh = model.ythresh
        # Apply a transformation to convert the raw margin values to probabilities
        yscore      = model.model.predict(Xpred)
        ypred_proba = 1 / (1 + np.exp( -model.alpha * yscore))  ### softmax
        ypred       = np.array([ 1 if p > ythresh else 0 for p in ypred_proba])
        return ypred, ypred_proba
        
    else :
        ypred       = model.model.predict(Xpred)
        ypred_proba = model.model.predict_proba(Xpred) 
        
    if merge_proba and len( ypred_proba.shape ) > 1 :
       ypred_proba = ypred_proba[:,1]
    return ypred, ypred_proba



def predict_proba(Xpred=None, data_pars={}, compute_pars={}, out_pars={},merge_proba=True, 
                  use_prepro=True, ythresh=0.5, **kw):
    global model, session

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro : 
        Xpred = model.prepro.transform(Xpred)
        log('predict_proba:Prepro Done:', Xpred.shape)
        
    if "LGBMRanker" in model.model_pars['model_class']:
        # Apply a transformation to convert the raw margin values to probabilities
        yscore       = model.model.predict(Xpred)  
        # ypred_proba = ypred 
        ypred_proba = 1 / (1 + np.exp( -model.alpha * yscore))  ### softmax
        return ypred_proba
        
    else :
        ypred_proba = model.model.predict_proba(Xpred)  
        if merge_proba :
           ypred_proba = ypred_proba[:,1]

        return ypred_proba



def save(path=None, info=None):
    global model, session
    #import cloudpickle as pickle
    import pickle
    # import cloudpickle as pickle
    os.makedirs(path, exist_ok=True)


    try :
       model2 = Model()
       model2.model_pars   = deepcopy(model.model_pars)
       model2.compute_pars = deepcopy(model.compute_pars)
       model2.data_pars    = deepcopy(model.data_pars)
       
       fout = f"{path}/model.pkl"
       with open(fout, mode='wb') as fp:
          pickle.dump(model2, fp,  protocol=pickle.HIGHEST_PROTOCOL )
          log(fout)    
    except Exception as e :
       log(e)


    try :
       fout = f"{path}/model_model.pkl"
       with open(fout, mode='wb') as fp:
          pickle.dump(model.model, fp , protocol=pickle.HIGHEST_PROTOCOL )
          log(fout)    
    except Exception as e :
       log(e)


    try :
       fout = f"{path}/model_prepro.pkl"
       joblib.dump(model.prepro, fout)
       log(fout)        
    except Exception as e :
       log(e)


    filename = "info.pkl"
    with open(f"{path}/{filename}", mode='wb') as fp:
       pickle.dump(info, fp , protocol=pickle.HIGHEST_PROTOCOL )



def load(path):
    load_model(path)
    load_info(path)


def load_model(path=""):
    # self.model_colsX = load(path + "/colsX.pkl" )
    # self.model_info  = load(path + "/info.pkl"  )
    global model, session
    import cloudpickle as pickle
    # import cloudpickle as pickle
    session = None

    #### Loadind Base Model ######################################
    fin = f"{path}/model.pkl"
    try  :
        # model0      = pickle.load(open(f"{path}/model.pkl", mode='rb'))
        # from pycaret.classification import load_model
        model0 = joblib.load(fin)
        print('loaded: ', fin, model0)        
        # model  = Model()  # Empty model

        try :
            model = Model(model0.model_pars)
            #model.model_pars = model0.model_pars
        except :
            model.model_pars = {}

        try :
            model.compute_pars = model0.compute_pars
        except :
            model.compute_pars = {}

        try :
            model.model = model0.model
        except :
            model.model = model0

        session = None

    except Exception as e :
        log(f'not loaded {fin}',e)


    ###### Loading Model      ##################################
    try  :
        fin     = f"{path}/model_model.pkl"
        model0 = joblib.load(fin)
        log('loaded: ', fin, model0)
        try :
            model.model = model0
        except :
            model.model = None
    except Exception as e :
       log(e)
       
    ###### Loading Preprocessing  #############################
    try  :
        fin     = f"{path}/model_prepro.pkl"
        prepro0 = joblib.load(fin)
        log('loaded: ', fin, prepro0)

        try :
            model.prepro = prepro0
        except :
            model.prepro = None
    except Exception as e :
       log(e)

    return model, session



def load_info(path=""):
    import cloudpickle as pickle, glob
    dd = {}
    for fp in glob.glob(f"{path}/*.pkl"):
        if not "model.pkl" in fp:
            obj = pickle.load(open(fp, mode='rb'))
            key = fp.split("/")[-1]
            dd[key] = obj


    model.info = dd 
    return dd




def preprocess(prepro_pars):
    if prepro_pars['type'] == 'test':
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split

        X, y = make_classification(n_features=10, n_redundant=0, n_informative=2,
                                   random_state=1, n_clusters_per_class=1)

        # log(X,y)
        Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)
        return Xtrain, ytrain, Xtest, ytest

    if prepro_pars['type'] == 'train':
        from sklearn.model_selection import train_test_split
        df = pd.read_csv(prepro_pars['path'])
        dfX = df[prepro_pars['colX']]
        dfy = df[prepro_pars['coly']]
        Xtrain, Xtest, ytrain, ytest = train_test_split(dfX.values, dfy.values,
                                                        stratify=dfy.values,test_size=0.1)
        return Xtrain, ytrain, Xtest, ytest

    else:
        df = pd.read_csv(prepro_pars['path'])
        dfX = df[prepro_pars['colX']]

        Xtest, ytest = dfX, None
        return None, None, Xtest, ytest


####################################################################################################
############ Do not change #########################################################################
def get_dataset(data_pars=None, task_type="train", **kw):
    """
      "ram"  : 
      "file" :
    """
    # log(data_pars)
    data_type = data_pars.get('type', 'ram')
    if data_type == "ram":
        if task_type == "predict":
            d = data_pars[task_type]
            return d["X"]

        if task_type == "eval":
            d = data_pars[task_type]
            return d["X"], d["y"]

        if task_type == "train":
            d = data_pars[task_type]
            return d["Xtrain"], d["ytrain"], d["Xtest"], d["ytest"]

    elif data_type == "file":
        raise Exception(f' {data_type} data_type Not implemented ')

    raise Exception(f' Requires  Xtrain", "Xtest", "ytrain", "ytest" ')


def get_params_sklearn(deep=False):
    return model.model.get_params(deep=deep)


def get_params(param_pars={}, **kw):
    import json
    # from jsoncomment import JsonComment ; json = JsonComment()
    pp = param_pars
    choice = pp['choice']
    config_mode = pp['config_mode']
    data_path = pp['data_path']

    if choice == "json":
        cf = json.load(open(data_path, mode='r'))
        cf = cf[config_mode]
        return cf['model_pars'], cf['data_pars'], cf['compute_pars'], cf['out_pars']

    else:
        raise Exception(f"Not support choice {choice} yet")





###################################################################################################
if __name__ == "__main__":
    fire.Fire()



