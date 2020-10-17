import tensorflow as tf
import os
from utils import utils


class machine_learning():
    
    def __init__(self):
        tf.enable_eager_execution()
        self.logger = utils.get_logger()
        self.logger.info("TensorFlow version: {}".format(tf.__version__))
        self.logger.info("Eager execution: {}".format(tf.executing_eagerly()))


    
    def predict(self):
        pass

    def train(self,filename):
        

        train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"

        train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),
                                                origin=train_dataset_url)

        self.logger.info("Local copy of the dataset file: {}".format(train_dataset_fp))

        column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

        feature_names = column_names[:-1]
        label_name = column_names[-1]

        self.logger.info("Features: {}".format(feature_names))
        self.logger.info("Label: {}".format(label_name))

        class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']

        batch_size = 32

        train_dataset = tf.data.experimental.make_csv_dataset(
            train_dataset_fp,
            batch_size,
            column_names=column_names,
            label_name=label_name,
            num_epochs=1)

        features, labels = next(iter(train_dataset))

        self.logger.info(features)
