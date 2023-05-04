import numpy as np
import pandas as pd
from datareader import Reader

class Stock():

    def __init__(self, ticker):
        # Initalize variables
        self.ticker = ticker
        self.reader = Reader(self.ticker)

        # Fill initial data
        raw_data = self.reader.get_daily_data()
        self.data = np.array(dict(raw_data['Time Series (Daily)']))

        

        