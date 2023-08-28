""" Training model
Docs::


        https://www.andrewvillazon.com/custom-scikit-learn-transformers/
        Category Encoders - a large set of Categorical Variable transformations.
        Feature Engine - excellent range of Numeric and Categorical variable transformations. Easy to use with a lot of useful functionality.
        sklearn-pandas - Useful library for mapping the results of a transformation back to a DataFrame.
        scikit-lego

        Feature-engine: A Python package that provides a set of transformers for feature engineering tasks.
        Scikit-learn-contrib: A collection of repositories that provides additional tools and utilities that complement Scikit-learn.
        Sklearn-pandas: This module provides a bridge between Scikit-Learn's machine learning methods and pandas-style Data Frames.
        MLxtend: This library provides additional utilities for machine learning
        https://feature-engine.trainindata.com/en/latest/


"""
import warnings
warnings.simplefilter(action='ignore')
import os, sys, time, traceback,copy, gc, shutil,json, traceback
from typing import Any, Callable, Sequence, Dict, List, Optional, Union
from copy import deepcopy
from box import Box
import fire, boto3, pandas as pd, numpy as np, awswrangler as wr


from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import (OneHotEncoder, StandardScaler, 
      KBinsDiscretizer, OrdinalEncoder)
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.feature_extraction import FeatureHasher  
from sklearn.compose import ColumnTransformer  

from utilmy import log 


def pd_generate_data(ncols=7, nrows=100):
    """ Generate sample data for function testing categorical features
    """
    np.random.seed(444)
    numerical    = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
    df = pd.DataFrame(numerical, columns = [str(i) for i in range(0,ncols)])
    df['cat1']= np.random.choice(  a=[0, 1],  size=nrows,  p=[0.7, 0.3]  )
    df['cat2']= np.random.choice(  a=[4, 5, 6],  size=nrows,  p=[0.5, 0.3, 0.2]  )
    df['cat1']= np.where( df['cat1'] == 0,'low',np.where(df['cat1'] == 1, 'High','V.High'))
    return df


def test():
    """

    """
    import utilmy as uu

    cc   = Box({})

    df = pd_generate_data(ncols=10, nrows=100)

    dftr = dfval = df
    cc.colused = df.columns 


    log("###### Train: Preprocessing start  ##############################")
    # from pycaret.classification import (setup, get_config, save_model)
    
    prepro1 = prepro_create_v1( colsnum1=     cc.colsnum1,     colsnum2= cc.colsnum2,  
                                colscat1none= cc.colscat1none, colscat2= cc.colscat2, 
                                colscat3= cc.colscat3, colscat4= cc.colscat4, 
                                colsnone= cc.colsnone, colsy=    cc.colsy,)
 
    ### Need to validate dtype
    X_train = prepro1.fit_transform(dftr[  cc.colused   ],  )
    X_train = sk_add_column(prepro1, X_train)
            
    X_test = prepro1.transform(dfval[ cc.colused  ])
    X_test = sk_add_column(prepro1, X_test)

    y_train = dftr[cc.colsy]
    y_test  = dfval[cc.colsy]
    

    log("######### Saving prepro_model    #####################################")
    import joblib
    #prepro_pipe = get_config('prep_pipe')
    log(prepro_pipe)
    joblib.dump(prepro_pipe, cc.prepro.dir_prepropipe )







def prepro_create_v1(colsnone=None, colsnum1=None, colsnum2=None,
                     colscat1none=None,colscat2=None,colscat3=None, colscat4=None, colsy=None, **kw):
  """
    https://towardsdatascience.com/getting-the-most-out-of-scikit-learn-pipelines-c2afc4410f1a

    # Create a custom pass-through function for the topics, since they are
    # already tokenized. We will only use CountVectorizer to split the topics
    # into separate feature columns.
    def no_analyzer(doc):
        Pass-through function to avoid transforming topics lists, which are 
        already tokenized.
        return doc

    ##### create ColumnTransformer, and pass the column names to transform in each step

    cols_trans = ColumnTransformer(transformers=[
        ('txt', TfidfVectorizer(), text_col),
        ('txt_kw', CountVectorizer(), topic_col),
        ('ohe', OneHotEncoder(drop='first'), cat_cols), 
    ],       remainder= 'passthrough'
    )
      clf = Pipeline(
          steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
      )


        # Create the pipeline by combining the column transformer with the LGMRanker model
    pipeline = Pipeline([
        ('preprocessing', column_transformer),
        ('model', LGBMRanker())
    ])

    ##### Fit the pipeline to your training data and labels
    pipeline.fit(X_train, y_train, model__group=group_train)

      from dirty_cat import (
      SimilarityEncoder,
      TargetEncoder,
      MinHashEncoder,
      GapEncoder,
    )

    encoders = {
        "one-hot": one_hot,
        "similarity": SimilarityEncoder(),
        "target": TargetEncoder(handle_unknown="ignore"),
        "minhash": MinHashEncoder(n_components=100),
        "gap": GapEncoder(n_components=100),
    }
        
    from pprint import pprint

    pprint(table_vec.transformers_)

    ###### Existing ColumnTransformer
    
    ct_existing = ColumnTransformer(
        transformers=[
            ('scaler', StandardScaler(), ['numerical_column']),
            ('encoder', OneHotEncoder(), ['categorical_column'])
        ]
    )

    # New transformer
    new_transformer = SomeTransformer()
    new_columns = ['new_column']

    # Get the existing transformers and columns
    transformers = ct_existing.transformers
    columns = ct_existing._columns

    # Append the new transformer and its columns
    transformers.append(('new_transformer', new_transformer, new_columns))
    columns.extend(new_columns)

    
  """

  prepro_colsnum1 = Pipeline(
      steps=[("scaler", StandardScaler() ) ]
  )

  prepro_colsnum2 = Pipeline(
      steps=[ ("binner",  KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile',)   )]
  )

  prepro_colscat2 = Pipeline(
      steps=[ ("encoder_int", Hasher64(n_dim=100, )
                                        # handle_unknown= 'use_encoded_value',
                                        # unknown_value =-1,
                                        #encoded_missing_value=-2,)
                                        #min_frequency=2)                         
              ),
      ] )


  prepro_colscat3 = Pipeline(
      steps=[ ("hasher", Hasher64(n_dim=100,) ),
      ] )


  prepro_colscat4 = Pipeline(
      steps=[ ("encoder_onehot", OneHotEncoder(categories='auto',drop='if_binary', handle_unknown="ignore",)
                                       # min_frequency=1)
                                       ),
              # ("selector", SelectPercentile(chi2, percentile=50)),  ## break at prediction time
      ])


  prepro_full = ColumnTransformer(
      transformers=[
          ("colsnum1",       prepro_colsnum1, list(colsnum1) ),   ### Normalization
          ("colsnum2",       prepro_colsnum2, list(colsnum2) ),   ### Binning into Ordinal

          ("colscat1none",   "passthrough",   list(colscat1none) ), ### Nothing
          # ("colscat2",       prepro_colscat2, list(colscat2) ),     ### Hashing String to Hashint
          ("colscat3",       prepro_colscat3, list(colscat3) ),    ### Hashing High Cardinatl, bug in hashing
          #("colscat4",      prepro_colscat4, list(colscat4) ),    ### One Hot Encoding                    
          #("colsnone",      "passthrough", list(colsnone) ), ### Pass Through        

          ("colsy",   "passthrough",   list(colsy) ), ### Nothing


          ],
      remainder= 'passthrough' , n_jobs=1
  )
  log(prepro_full)
  return prepro_full



class Hasher64(BaseEstimator, TransformerMixin):
    def __init__(self, n_dim=128):
        """
      
            h = Hasher64()
            df['a_hashed'] = h.transform(df['a'])
            print(df)        
            
        """
        self.n_dim = n_dim
        self.cols = []

    def fit(self, X, y=None):
        self.cols = list(X.columns)
        return self

    def transform(self, X):        
        self.cols = list(X.columns)
        
        n_dim   = self.n_dim
        if len(X.shape) == 1 or X.shape[1] < 1:
            return np.array([hash_int64(str(x)) % n_dim for x in X.values]).astype("int64")
        else:
            X2 = np.zeros_like(X.values).astype("int64") 
            for j in range(X.shape[1]):
               X2[:,j] = [ hash_int64(str(xi))  % n_dim for xi in X.values[:,j] ]
            return X2  

    def get_feature_names(self):
      return self.cols



def sk_add_column(prepro1, df, dtypes:dict=None):
    """ Adds columns to sklearn output

    Args:
        prepro1: The preprocessor used to transform the data.
        df: The DataFrame to which the column will be added.
        dtypes (optional): A dictionary specifying the data types for the columns. Defaults to None.

    Returns:
        df: The DataFrame with the added column.
    """    
    colsall = []    
    for vi in prepro1.transformers_[:]:
        log(vi[0])
        colsall = colsall + vi[2] 
    log('Ncols:', len(colsall ))    
    
    # df = np.array(df, dtype='float32')
    df = pd.DataFrame(df, columns=colsall)    
    
    dtypes = {} if dtypes is None else dtypes
    for ci in df.columns : 
        if ci in dtypes:
            di = str(dtypes[ci])
            if   'int32'    in di : df[ci] = df[ci].astype('int32') 
            elif 'float32'  in di : df[ci] = df[ci].astype('float32') 
            elif 'float64'  in di : df[ci] = df[ci].astype('float64') 
            elif 'int64'    in di : df[ci] = df[ci].astype('int64') 
            elif 'object'   in di : df[ci] = df[ci].astype('int64')             
            elif 'string'   in di : df[ci] = df[ci].astype('int64')             
            else : 
                df[ci] = df[ci].astype('float32') 
                
    ### Remove duplicates column 
    # df.set_flags(allows_duplicate_labels=False)    
    df = df.loc[:,~df.columns.duplicated()].copy()
    log(df.dtypes)
    return df 

#################################################################################
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def sk_pipe_transform(df, pipeline):
    """
    Applies a Pipeline to a pandas DataFrame and returns a new DataFrame with the correct column names.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    pipeline (Pipeline): The Pipeline to apply.
    
    Returns:
    pd.DataFrame: The transformed DataFrame with the correct column names.
    """
    # Apply the Pipeline
    transformed_data = pipeline.transform(df)
    
    # Get the column names from the last transformer in the pipeline
    last_transformer = pipeline.named_steps[pipeline.steps[-1][0]]
    columns = []
    
    if isinstance(last_transformer, ColumnTransformer):
        for name, trans, column in last_transformer.transformers_:
            if trans == 'drop':
                continue
            elif trans == 'passthrough':
                columns.extend(df.columns[column])
            else:
                columns.extend([f"{name}_{colname}" for colname in trans.get_feature_names_out()])
    else:
        columns = last_transformer.get_feature_names_out()
    
    # Create a new DataFrame with the transformed data and the correct column names
    transformed_df = pd.DataFrame(transformed_data, columns=columns)
    
    return transformed_df


def sk_transfrom(prepro1,  df, cols=None):
    """Applies a ColumnTransformer to a pandas DataFrame and returns a new DataFrame with the correct column names.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    transformer (ColumnTransformer): The ColumnTransformer to apply.
    
    Returns:
    pd.DataFrame: The transformed DataFrame with the correct column names.
    """
    
    cols = list(df.columns) if cols is None else cols
    X_train = prepro1.fit_transform(df[cols],  )
    colsall = []    
    for vi in prepro1.transformers_[:]:
        log('prepro name', vi[0]) ###
        ptype = str(vi[1])
        if 'OneHot' in ptype:
            pass
        colsall = colsall + vi[2] 
    #log(len(     colsall ))    
    X_train  = pd.DataFrame(X_train, columns=colsall)    
    return X_train 

    # columns = []
    # for name, trans, column in transformer.transformers_:
    #     if trans == 'drop':
    #         continue
    #     elif trans == 'passthrough':
    #         columns.extend(df.columns[column])
            
    #     elif trans == 'remainder':
    #         columns.extend(df.columns[column])

    #     else:
    #         columns.extend([f"{name}_{colname}" for colname in trans.get_feature_names_out()])
    
    # transformed_df = pd.DataFrame(transformed_data, columns=columns)    
    # return transformed_df




##################################################################################
import sklearn
from sklearn.preprocessing import OrdinalEncoder

class MultiplyColumns(BaseEstimator, TransformerMixin):
    def __init__(self, by=1, columns=None):
        self.by = by
        self.columns = columns
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        cols_to_transform = list(X.columns)

        if self.columns:
            cols_to_transform = self.columns

        X[cols_to_transform] = X[cols_to_transform] * self.by
        return X
    

class CustomOrdinalEncoder(OrdinalEncoder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def transform(self, X, y=None):
        transformed_X = super().transform(X)
        new_X = pd.DataFrame(transformed_X, columns=self.feature_names_in_)

        return new_X


class ColumnTransformerWithNames(ColumnTransformer):        
    def get_feature_names(column_transformer):
        """Get feature names from all transformers.
        Returns
        -------
        feature_names : list of strings
            Names of the features produced by transform.
        """
        # Remove the internal helper function
        #check_is_fitted(column_transformer)

        # Turn loopkup into function for better handling with pipeline later
        def get_names(trans):
            # >> Original get_feature_names() method
            if trans == 'drop' or (
                    hasattr(column, '__len__') and not len(column)):
                return []
            if trans == 'passthrough':
                if hasattr(column_transformer, '_df_columns'):
                    if ((not isinstance(column, slice))
                            and all(isinstance(col, str) for col in column)):
                        return column
                    else:
                        return column_transformer._df_columns[column]
                else:
                    indices = np.arange(column_transformer._n_features)
                    return ['x%d' % i for i in indices[column]]
            if not hasattr(trans, 'get_feature_names'):
            # >>> Change: Return input column names if no method avaiable
                # Turn error into a warning
    #             warnings.warn("Transformer %s (type %s) does not "
    #                                  "provide get_feature_names. "
    #                                  "Will return input column names if available"
    #                                  % (str(name), type(trans).__name__))
                # For transformers without a get_features_names method, use the input
                # names to the column transformer
                if column is None:
                    return []
                else:
                    return [#name + "__" + 
                            f for f in column]

            return [#name + "__" + 
                    f for f in trans.get_feature_names()]

        ### Start of processing
        feature_names = []

        # Allow transformers to be pipelines. Pipeline steps are named differently, so preprocessing is needed
        if type(column_transformer) == sklearn.pipeline.Pipeline:
            l_transformers = [(name, trans, None, None) for step, name, trans in column_transformer._iter()]
        else:
            # For column transformers, follow the original method
            l_transformers = list(column_transformer._iter(fitted=True))


        for name, trans, column, _ in l_transformers: 
            if type(trans) == sklearn.pipeline.Pipeline:
                # Recursive call on pipeline
                _names = column_transformer.get_feature_names(trans)
                # if pipeline has no transformer that returns names
                if len(_names)==0:
                    _names = [#name + "__" + 
                              f for f in column]
                feature_names.extend(_names)
            else:
                feature_names.extend(get_names(trans))

        return feature_names
        
    def transform(self, X):
        indices = X.index.values.tolist()
        original_columns = X.columns.values.tolist()
        X_mat = super().transform(X)
        new_cols = self.get_feature_names()
        new_X = pd.DataFrame(X_mat.toarray(), index=indices, columns=new_cols)
        return new_X

    def fit_transform(self, X, y=None):
        super().fit_transform(X, y)
        return self.transform(X)



from itertools import chain
from numbers import Integral
import scipy.sparse as sp
#from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.base import BaseEstimator, TransformerMixin


def _iteritems(d):
    """Like d.iteritems, but accepts any collections.Mapping."""
    return d.iteritems() if hasattr(d, "iteritems") else d.items()


class Hasher(BaseEstimator, TransformerMixin):    
    def __init__(self, n_dim=100):
        """# Initialize Hasher and transform the 'a' column
            df = pd.DataFrame({'a':['string1','string2','string3']})
            h = Hasher()
            df['a_hashed'] = h.transform(df['a'])
            print(df)
        """
        self.n_dim = n_dim
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Ensure the output is int32
        return np.array([ hash_int64(str(x)) % self.n_dim for x in X]).astype(np.int64)



class FeatureHasher_int32(TransformerMixin, BaseEstimator):
    """Implements feature hashing, aka the hashing trick.

    Parameters
    ----------
    n_features : int, default=2**20
        The number of features (columns) in the output matrices. Small numbers
        of features are likely to cause hash collisions, but large numbers
        will cause larger coefficient dimensions in linear learners.
    input_type : str, default='dict'
        Choose a string from {'dict', 'pair', 'string'}.
        Either "dict" (the default) to accept dictionaries over
        (feature_name, value); "pair" to accept pairs of (feature_name, value);
        or "string" to accept single strings.
        feature_name should be a string, while value should be a number.
        In the case of "string", a value of 1 is implied.
        The feature_name is hashed to find the appropriate column for the
        feature. The value's sign might be flipped in the output (but see
        non_negative, below).
    dtype : numpy dtype, default=np.float64
        The type of feature values. Passed to scipy.sparse matrix constructors
        as the dtype argument. Do not set this to bool, np.boolean or any
        unsigned integer type.
        
    Examples
    >>> h = FeatureHasher(n_features=8, input_type="string")
    >>> raw_X = [["dog", "cat", "snake"], ["snake", "dog"], ["cat", "bird"]]
    >>> f = h.transform(raw_X)
    >>> f.toarray()
    """

    # _parameter_constraints: dict = {
    #     "n_features": [Interval(Integral, 1, np.iinfo(np.int32).max, closed="both")],
    #     "input_type": [StrOptions({"dict", "pair", "string"})],
    #     "dtype": "no_validation",  # delegate to numpy
    #     "alternate_sign": ["boolean"],
    # }

    def __init__(
        self,
        n_features=(2**20),
        *,
        input_type="dict",
        dtype=np.float64,
        alternate_sign=True,
    ):
        self.dtype = dtype
        self.input_type = input_type
        self.n_features = n_features
        self.alternate_sign = alternate_sign

    #@_fit_context(prefer_skip_nested_validation=True)
    def fit(self, X=None, y=None):
        """Only validates estimator's parameters.
        """
        return self

    def transform(self, raw_X):
        """Transform a sequence of instances to a scipy.sparse matrix.

        Parameters
        ----------
        raw_X : iterable over iterable over raw features, length = n_samples
            Samples. Each sample must be iterable an (e.g., a list or tuple)
            containing/generating feature names (and optionally values, see
            the input_type constructor argument) which will be hashed.
            raw_X need not support the len function, so it can be the result
            of a generator; n_samples is determined on the fly.

        Returns
        -------
        X : numpy shape (n_samples, 1)
            Feature matrix, for use with estimators or further transformers.
        """
        raw_X = iter(raw_X)
        if self.input_type == "dict":
            raw_X = (_iteritems(d) for d in raw_X)
        elif self.input_type == "string":
            first_raw_X = next(raw_X)
            if isinstance(first_raw_X, str):
                raise ValueError(
                    "Samples can not be a single string. The input must be an iterable"
                    " over iterables of strings."
                )
            from itertools import chain
            from numbers import Integral                

            raw_X = chain([first_raw_X], raw_X)

        nfeat =  self.n_features
        X = np.array([ [ hash_int32(str(xi)) %  nfeat for xi in vk] for vk in raw_X ])
        return X

    def _more_tags(self):
        return {"X_types": [self.input_type]}







###################################################################################################
if __name__ == "__main__":
    fire.Fire()




