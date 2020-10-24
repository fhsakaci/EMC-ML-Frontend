import os
import pandas as pd
from utils import utils
import numpy as np
import urllib.request as request
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

class machine_learning():
    
    def __init__(self):
        self.logger = utils.get_logger()
        self.logger.info("TensorFlow version: {}".format(tf.__version__))
        self.logger.info("Eager execution: {}".format(tf.executing_eagerly()))


    def train(self,filename):
        self.logger.debug(str(filename))
        train_dataset_fp = pd.read_csv(filename)
        self.logger.debug(train_dataset_fp.head())
        self.logger.info("Local copy of the dataset file: {}".format(train_dataset_fp))

        features = train_dataset_fp.copy()
        labels = features.pop('Level')


        self.logger.info("Features: {}".format(features))
        self.logger.info("Label: {}".format(labels))

        
        model = tf.keras.Sequential([
        layers.Dense(60),
        layers.Dense(15),
        layers.Dense(5),
        layers.Dense(1),
        ])

        model.compile(loss='mean_squared_error',
                            optimizer = tf.optimizers.Adam(),
                            metrics=['accuracy'])
        model.fit(features, labels, epochs=50,batch_size= 64,validation_split=0.2)
        return model    

    def predict(self,path):
        dataset = []
        for i in range(150000,1000000,100):
            print(i)
            data=tf.constant([10, 30, 70000, i])
            dataset.append(data)
        
        x = tf.stack([dataset])
        print(x)
        loaded_model = tf.keras.models.load_model(path)
        return loaded_model.predict(x)
