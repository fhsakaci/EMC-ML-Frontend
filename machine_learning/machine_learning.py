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


    
    def predict(self):
        pass

    def train(self,filename):
        self.logger.debug(str(filename))
        train_dataset_fp = pd.read_csv(filename)
        self.logger.debug(train_dataset_fp.head())
        self.logger.info("Local copy of the dataset file: {}".format(train_dataset_fp))

        features = train_dataset_fp.copy()
        labels = features.pop('Value')


        self.logger.info("Features: {}".format(features))
        self.logger.info("Label: {}".format(labels))

        
        model = tf.keras.Sequential([
        layers.Dense(64),
        layers.Dense(1)
        ])

        model.compile(loss = tf.losses.MeanSquaredError(),
                            optimizer = tf.optimizers.Adam())


        model.fit(features, labels, epochs=10)

        model.save("saved_model/my_model")

    def predict(self,filename):
        loaded_model = tf.keras.models.load_model(filename)
