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
        # self.model = tf.keras.models.load_model(f'/model/{self.ticker}.h5')

        # Fill initial data
        self.current_price = None
        self.chart_data = None

    def get_data(self):
        self.chart_data = self.reader.get_all_data(for_chart=True)
        self.current_price = self.chart_data[-1]['close']
        


    # def __predict__(self, data):
    #     prediction = self.model.predict(data)
    #     if prediction >= self.cuurent_price:
    #         return True
    #     return False
    