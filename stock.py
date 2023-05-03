import numpy as np
import pandas as pd
from datareader import Reader

class Stock():

    def __init__(self, ticker, time_frame):
        # Initalize variables
        self.ticker = ticker
        self.time_frame = time_frame
        self.reader = Reader(self.ticker, self.time_frame)

        # Fill initial data
        raw_data = self.reader.get_daily_data()
        self.data = np.array(dict(raw_data['Time Series (Daily)']))

        

        