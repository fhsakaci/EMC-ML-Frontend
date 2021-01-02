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

        
        normalizer = preprocessing.Normalization()
        normalizer.adapt(np.array(features))
        model = tf.keras.Sequential([
            normalizer,
            layers.Dense(256, activation='relu'),
            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(32, activation='sigmoid'),
            layers.Dense(1)
        ])
        

        model.summary()

        
        
        model.compile(
                optimizer=tf.optimizers.Adam(0.001),
                loss='mean_squared_error',
                metrics=['accuracy'])
        ##time
        model.fit(
            features, labels, 
            epochs=1000,
            # suppress logging
            verbose=0,
            # Calculate validation results on 20% of the training data
            validation_split = 0.2)

        self.logger.info("Model has been created")
        return model    

    def predict(self,path):
        dataset = []
        for i in range(150000,1000000,100):
            data=tf.constant([10, 30, 70000, i])
            dataset.append(data)
        
        x = tf.stack([dataset])
        loaded_model = tf.keras.models.load_model(path)
        return loaded_model.predict(x)
