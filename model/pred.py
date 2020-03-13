# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:16:52 2019

@author: somous
"""

import glob
import os
import numpy as np
import pandas as pd
from keras.models import load_model
import tensorflow as tf
from keras.utils import to_categorical as categorical
import pandas as pd


def modelLoad(file):
    print('**************load '+ file+' **************model!')
    model = load_model(file)
    return model


def main():

    file = 'data_to_pred.csv' # here specify the data filename that need to predict
    
    data = pd.read_csv(file,index_col=0)
    index = data.index
    data = data.values
    config = tf.ConfigProto()
    config.gpu_options.allow_growth=True
    set_session(tf.Session(config=config))
    os.environ["CUDA_VISIBLE_DEVICES"] = "0" # specify gpu 0 or 1
    
    modelfile = 'Model.h5'
    model = modelLoad(modelfile)
    pred = model.predict_proba(data)
    pred = pd.DataFrame(pred)
        
    pred.index = index
    pred.to_csv('pred.csv')
    
    
if __name__ =='__main__':
    main()
