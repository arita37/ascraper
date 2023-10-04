# -*- coding: utf-8 -*-
""" Model template

CatBoostRanker:

   from catboost import CatBoostRanker
   clf = CatBoostRanker()

"""

import os, json, fire, joblib
import pandas as pd, numpy as np, cloudpickle as pickle 

from copy import deepcopy
from catboost import CatBoostRanker, Pool
from utilmy import pd_read_file, pd_to_file, log, log2, pd_generate_data2

# Global variables
global model


def init(*kw, **kwargs):
    global model
    model = Model(*kw, **kwargs)


def reset():
    global model
    model = None



################################################################################
def test():
    global model, session
    dirin = "ztmp/local/models/0_Extra/"

    # Use the new data generation function
    dftrain = pd_generate_data2(n_colnum=3, n_colcat=4, nrows=100, use_catstr=1)
    ytrain  = np.random.randint(0, 2, 100)

    # Generate synthetic RankGroup data (you need to adjust this based on your specific data structure)
    Xtrain_rankgroup = np.array([0] * 50 + [1] * 50)  # Example: Two groups


    dfval   = pd_generate_data2(n_colnum=3, n_colcat=4, nrows=50, use_catstr=1)
    yval    = np.random.randint(0, 2, 50)
    # Generate synthetic RankGroup data (you need to adjust this based on your specific data structure)
    Xtest_rankgroup  = np.array([0] * 25 + [1] * 25)  # Example: Two groups for validation


    # Define the model parameters
    model_pars = {
        "model_class": "CatBoostRanker",
        "model_pars": {
            "iterations": 100,
            "learning_rate": 0.1,
            "depth": 6,
        },
        "alpha": 1.0,
        "ythresh": 0.5
    }

    # Initialize the model
    init(model_pars=model_pars)
    
    fit(Xtrain=dftrain, ytrain=ytrain, Xtest=dfval, ytest=yval,
        Xtrain_rankgroup=Xtrain_rankgroup, Xtest_rankgroup=Xtest_rankgroup)
        
    proba_ = predict_proba(dfval)
    predict_ = predict_all(dfval)

    # Save the model and info
    save("model_directory", info={"description": "My Model"})

    # Load the model and info
    load("model_directory")
    proba_ = predict_proba(dfval)

    

class Model(object):
    def __init__(self, model_pars=None, data_pars=None, compute_pars=None):
        self.model_pars.  = model_pars if model_pars is not None else {}
        self.compute_pars = compute_pars if compute_pars is not None else {}
        self.data_pars    = data_pars if data_pars is not None else {}
        self.info = {}

        self.ythresh = 0.5
        self.alpha   = 1.0

        self.model  = None
        self.prepro = None

        if model_pars is not None:
            try:
                self.ythresh = model_pars.get('ythresh', 0.5)
                self.alpha = model_pars.get('alpha', 1.0)

                self.model = CatBoostRanker(**model_pars.get('model_pars', {}))

                log2("Initialized CatBoost Model:", self.model)
            except Exception as e:
                log(e)
                self.model = None


def fit(Xtrain=None, ytrain=None, Xtest=None, ytest=None,
        Xtrain_rankgroup=None, Xtest_rankgroup=None, #These for CatBoostranker
        compute_pars=None, out_pars=None, use_prepro=False, ww=None, **kw):
    global model
    compute_pars = {} if compute_pars is None else compute_pars

    if use_prepro and model.prepro is not None:
        Xtrain = model.prepro.transforms(Xtrain)
        Xtest = model.prepro.transforms(Xtest)
        print('fit: prepro done:', Xtrain.shape)

    print('Data Train shape:', Xtrain.shape, Xtest.shape)

    # Fit the CatBoostRanker with ranking groups provided as 'group_id'
    train_pool = Pool(Xtrain, label=ytrain, group_id=Xtrain_rankgroup)
    test_pool  = Pool(Xtest, label=ytest, group_id=Xtest_rankgroup)
    model.model.fit(train_pool, eval_set=test_pool, **compute_pars)

def predict_all(Xpred=None, data_pars=None, compute_pars=None, out_pars=None, use_prepro=False, **kw):
    
    global model

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro:
        Xpred = model.prepro.transform(Xpred)
        print('predict_proba: Prepro Done:', Xpred.shape)

    ythresh = model.ythresh
    yscore = model.model.predict(Xpred)
    ypred_proba = 1 / (1 + np.exp(-model.alpha * yscore))
    ypred = np.array([1 if p > ythresh else 0 for p in ypred_proba])

    return ypred


def predict_proba(Xpred=None, data_pars=None, compute_pars=None, out_pars=None, use_prepro=False, **kw):
    global model

    if Xpred is None:
        data_pars['train'] = False
        Xpred = get_dataset(data_pars, task_type="predict")

    if model.prepro is not None and use_prepro:
        Xpred = model.prepro.transform(Xpred)
        print('predict_proba: Prepro Done:', Xpred.shape)

    yscore = model.model.predict(Xpred)
    ypred_proba = 1 / (1 + np.exp(-model.alpha * yscore))

    return ypred_proba


def save(path=None, info=None):
    global model

    os.makedirs(path, exist_ok=True)

    try:
        model2 = Model()
        model2.model_pars = deepcopy(model.model_pars)
        model2.compute_pars = deepcopy(model.compute_pars)
        model2.data_pars = deepcopy(model.data_pars)

        fout = f"{path}/model.pkl"
        with open(fout, mode='wb') as fp:
            pickle.dump(model2, fp)#, protocol=pickle.HIGHEST_PROTOCOL)
            print(fout)
    except Exception as e:
        print(e)

    try:
        fout = f"{path}/model_model.pkl"
        with open(fout, mode='wb') as fp:
            pickle.dump(model.model)#, fp, protocol=pickle.HIGHEST_PROTOCOL)
            print(fout)
    except Exception as e:
        print(e)

    try:
        fout = f"{path}/model_prepro.pkl"
        joblib.dump(model.prepro, fout)
        print(fout)
    except Exception as e:
        print(e)

    filename = "info.pkl"
    with open(f"{path}/{filename}", mode='wb') as fp:
        pickle.dump(info, fp)#, protocol=pickle.HIGHEST_PROTOCOL)


def load(path):
    load_model(path)
    load_info(path)


def load_model(path=""):
    global model

    try:
        fin = f"{path}/model.pkl"
        model0 = joblib.load(fin)
        print('loaded:', fin, model0)

        try:
            model = Model(model0.model_pars)
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

    except Exception as e:
        print(f'not loaded {fin}', e)

    try:
        fin = f"{path}/model_model.pkl"
        model0 = joblib.load(fin)
        print('loaded:', fin, model0)
        try:
            model.model = model0
        except:
            model.model = None
    except Exception as e:
        print(e)

    try:
        fin = f"{path}/model_prepro.pkl"
        prepro0 = joblib.load(fin)
        print('loaded:', fin, prepro0)

        try:
            model.prepro = prepro0
        except:
            model.prepro = None
    except Exception as e:
        print(e)

    return model


def load_info(path=""):
    import glob
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

        Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)
        return Xtrain, ytrain, Xtest, ytest

    if prepro_pars['type'] == 'train':
        from sklearn.model_selection import train_test_split
        df = pd.read_csv(prepro_pars['path'])
        dfX = df[prepro_pars['colX']]
        dfy = df[prepro_pars['coly']]
        Xtrain, Xtest, ytrain, ytest = train_test_split(dfX.values, dfy.values,
                                                        stratify=dfy.values, test_size=0.1)
        return Xtrain, ytrain, Xtest, ytest

    else:
        df = pd.read_csv(prepro_pars['path'])
        dfX = df[prepro_pars['colX']]

        Xtest, ytest = dfX, None
        return None, None, Xtest, ytest


if __name__ == "__main__":
    fire.Fire()
