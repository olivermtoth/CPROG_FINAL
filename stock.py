import numpy as np
import pandas as pd
from datareader import Reader
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Stock():

    def __init__(self, ticker):
        # Initalize variables
        self.ticker = ticker
        self.reader = Reader(self.ticker)
        self.model = tf.keras.models.

        # Fill initial data
        self.price = self.reader.get_all_data()['price']
        self.current_price = self.reader.get_current_price()


    def __predict__(self, data):
        prediction = self.model.predict(data)
        if prediction >= self.price:
            return True
        return False