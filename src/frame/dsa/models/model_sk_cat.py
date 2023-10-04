# -*- coding: utf-8 -*-
""" Model template

CatBoostClassifier:




"""

import os, json, fire, joblib
import numpy as np, pandas as pd, cloudpickle as pickle

from copy import deepcopy
from catboost import CatBoostClassifier  # Import CatBoostClassifier

####################################################################################################
# from src.utils.utilmy_log import log, log2
from utilmy import pd_read_file, pd_to_file, log, log2, pd_generate_data2



####################################################################################################
global model, session

def init(*kw, **kwargs):
    global model, session
    model = Model(*kw, **kwargs)
    session = None

def reset():
    global model, session
    model, session = None, None



####################################################################################################
def test1():
    global model, session
    dirin = "ztmp/local/models/0_Extra/"

    # Use the new data generation function
    dftrain = pd_generate_data2(n_colnum=3, n_colcat=4, nrows=100, use_catstr=1)
    dfval   = pd_generate_data2(n_colnum=3, n_colcat=4, nrows=50, use_catstr=1)
    ytrain  = np.random.randint(0, 2, 100)
    yval    = np.random.randint(0, 2, 50)

    # Define the model parameters
    model_pars = {
        "model_class": "CatBoostClassifier",  # Change to "CatBoostRegressor" for regression
        "model_pars": {
            "iterations": 100,
            "learning_rate": 0.1,
            "depth": 6,
        },
        "alpha": 1.0,  # Add your alpha parameter here
        "ythresh": 0.5  # Add your ythresh parameter here
    }

    # Initialize the model
    init(model_pars=model_pars)

    # Pass both training and testing data to the fit function
    fit(dftrain, ytrain, Xtest=dfval, ytest=yval)
    dfproba = predict_proba(dfval)

    # Save the model and info
    save("ztmp/", info={"description": "My Model"})

    # Load the model and info
    load("ztmp/")
    dfy = predict_all(dfval)



class Model(object):
    def __init__(self, model_pars=None, data_pars=None, compute_pars=None):
        self.model_pars   = model_pars if model_pars is not None else {}
        self.compute_pars = compute_pars if compute_pars is not None else {}
        self.data_pars    = data_pars if data_pars is not None else {}
        self.info = {}

        ### Proba Model
        self.ythresh = 0.5
        self.alpha   = 1.0
        self.model   = None
        self.prepro  = None

        if model_pars is not None:
            try:
                self.ythresh = model_pars.get('ythresh', 0.5)
                self.alpha   = model_pars.get('alpha', 1.0)

                self.model   = CatBoostClassifier(**model_pars['model_pars'])  # Create a CatBoostClassifier model
                log2(CatBoostClassifier, self.model)

            except Exception as e:
                log(e)
                self.model = None

def fit(Xtrain=None, ytrain=None, data_pars=None, Xtest=None, ytest=None,
        Xtrain_rankgroup=None, Xtest_rankgroup=None, compute_pars=None, out_pars=None, use_prepro=False, **kw):
    """
    """
    global model, session
    compute_pars = {} if compute_pars is None else compute_pars

    if Xtrain is None:
        Xtrain, ytrain, Xtest, ytest = get_dataset(data_pars, task_type="train")

    if use_prepro and model.prepro is not None:
        Xtrain = model.prepro.transforms(Xtrain)
        Xtest  = model.prepro.transforms(Xtest)
        log('fit:prepro done:', Xtrain.shape)

    log(Xtrain.head(5))
    log('Data Train shape: ', Xtrain.shape, Xtest.shape)

    # assert Xtest is None, log('Xtest is None')
    model.model.fit(Xtrain, ytrain,
                    eval_set=[(Xtest, ytest)],
                    early_stopping_rounds=model.model_pars.get('early_stopping_rounds', 10),
                    **compute_pars.get("compute_pars", {}))


def predict(Xpred=None, data_pars={}, compute_pars={}, out_pars={}, use_prepro=False, output_binary=False, **kw):
    global model, session

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro:
        Xpred = model.prepro.transform(Xpred)
        log('predict_proba:Prepro Done:', Xpred.shape)

    ypred = model.model.predict(Xpred)
    return ypred


def predict_all(Xpred=None, data_pars={}, compute_pars={}, out_pars={}, merge_proba=True, ythresh=0.5, use_prepro=False, **kw):
    global model, session

    if model.prepro is not None:
        Xpred = model.prepro.transform(Xpred)

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro:
        Xpred = model.prepro.transform(Xpred)
        log('predict_proba:Prepro Done:', Xpred.shape)

    ypred = model.model.predict(Xpred)
    ypred_proba = model.model.predict_proba(Xpred)

    if merge_proba and len(ypred_proba.shape) > 1:
        ypred_proba = ypred_proba[:, 1]
    return ypred, ypred_proba


def predict_proba(Xpred=None, data_pars={}, compute_pars={}, out_pars={}, merge_proba=True,
                  use_prepro=True, ythresh=0.5, **kw):
    global model, session

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro:
        Xpred = model.prepro.transform(Xpred)
        log('predict_proba:Prepro Done:', Xpred.shape)

    ypred_proba = model.model.predict_proba(Xpred)
    if merge_proba:
        ypred_proba = ypred_proba[:, 1]

    return ypred_proba


def save(path=None, info=None):
    global model, session
    # import cloudpickle as pickle
    import pickle
    os.makedirs(path, exist_ok=True)

    try:
        model2 = Model()
        model2.model_pars = deepcopy(model.model_pars)
        model2.compute_pars = deepcopy(model.compute_pars)
        model2.data_pars = deepcopy(model.data_pars)

        fout = f"{path}/model.pkl"
        with open(fout, mode='wb') as fp:
            pickle.dump(model2, fp, protocol=pickle.HIGHEST_PROTOCOL)
            log(fout)
    except Exception as e:
        log(e)

    try:
        fout = f"{path}/model_model.pkl"
        with open(fout, mode='wb') as fp:
            pickle.dump(model.model, fp, protocol=pickle.HIGHEST_PROTOCOL)
            log(fout)
    except Exception as e:
        log(e)

    try:
        fout = f"{path}/model_prepro.pkl"
        joblib.dump(model.prepro, fout)
        log(fout)
    except Exception as e:
        log(e)

    filename = "info.pkl"
    with open(f"{path}/{filename}", mode='wb') as fp:
        pickle.dump(info, fp)  # ,protocol=pickle.HIGHEST_PROTOCOL )

def load(path):
    load_model(path)
    load_info(path)

def load_model(path=""):
    global model, session
    session = None

    #### Loadind Base Model ######################################
    try:
        # model0      = pickle.load(open(f"{path}/model.pkl", mode='rb'))
        #from pycaret.classification import load_model
        
        fin = f"{path}/model.pkl"
        model0 = joblib.load(fin)
        print('loaded: ', fin, model0)
        # model  = Model()  # Empty model

        try:
            model = Model(model0.model_pars)
            # model.model_pars = model0.model_pars
        except:
            model.model_pars = {}

        try:
            model.compute_pars = model0.compute_pars
        except:
            model.compute_pars = {}

        try:
            model.model = model0.model
        except:
            model.model = model0

        session = None

    except Exception as e:
        log('load error', e)

    ###### Loading Model      ##################################
    try:
        fin = f"{path}/model_model.pkl"
        model0 = joblib.load(fin)
        log('loaded: ', fin, model0)
        try:
            model.model = model0
        except:
            model.model = None
    except Exception as e:
        log(e)

    ###### Loading Preprocessing  #############################
    try:
        fin = f"{path}/model_prepro.pkl"
        prepro0 = joblib.load(fin)
        log('loaded: ', fin, prepro0)

        try:
            model.prepro = prepro0
        except:
            model.prepro = None
    except Exception as e:
        log(e)

    return model, session

def load_info(path=""):
    import cloudpickle as pickle
    import glob
    dd = {}
    for fp in glob.glob(f"{path}/*.pkl"):
        if not "model.pkl" in fp:
            obj = pickle.load(open(fp, mode='rb'))
            key = fp.split("/")[-1]
            dd[key] = obj

    model.info = dd
    return dd



####################################################################################################
############ Do not change #########################################################################

def get_dataset(data_pars=None, task_type="train", **kw):
    """
      "ram"  : 
      "file" :
    """
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

if __name__ == "__main__":
    fire.Fire()
