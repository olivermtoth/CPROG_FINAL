"""
Getting data via https://www.alphavantage.co/ API
"""
import requests
from datetime import date, timedelta
import numpy as np
import finnhub
import time



class Reader():

    def __init__(self, ticker):
        """
        Initalizing Reader object to acsess market data.
        """
        with open('API_KEY', 'r', encoding='utf-8') as f:
            self.apikey = f.readline()
            f.close()
        with open('API_KEY1', 'r', encoding='utf-8') as f:
            self.apikey1 = f.readline()
            f.close()
        self.finnhub = finnhub.Client(self.apikey1)
        self.ticker = ticker


    def get_daily_data(self):
        """
        Get daily adjusted price
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&apikey={self.apikey}'
        data = requests.get(url,timeout=5).json()
        yesterday = str(date.today()-timedelta(days = 1))
        return data["Time Series (Daily)"][yesterday]['5. adjusted close']
    
    def get_100_data(self):
        """
        Get data from the last 100 day
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&&apikey={self.apikey}'
        raw_data = requests.get(url,timeout=5).json()
        # f = open('sample.json')
        # raw_data = json.load(f)
        
        # https://stackoverflow.com/a/44815276
        # https://stackoverflow.com/a/11001347
        dates = list(raw_data["Time Series (Daily)"].keys())
        start_date = time.mktime(time.strptime(dates[0], '%Y-%m-%d'))
        end_date = time.mktime(time.strptime(dates[-1], '%Y-%m-%d'))

        adjusted_price = np.array([
            [float(raw_data["Time Series (Daily)"][x]['5. adjusted close']) for x in raw_data["Time Series (Daily)"]],
            [float(raw_data["Time Series (Daily)"][x]['6. volume']) for x in raw_data["Time Series (Daily)"]]
        ])
        return adjusted_price
    
    def get_all_data(self):
        """
        Get the full available historical price
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&outputsize=full&apikey={self.apikey}'
        raw_data = requests.get(url,timeout=5).json()
        # f = open('sample.json')
        # raw_data = json.load(f)
        adjusted_price = np.array([
            [float(raw_data["Time Series (Daily)"][x]['5. adjusted close']) for x in raw_data["Time Series (Daily)"]],
            [float(raw_data["Time Series (Daily)"][x]['6. volume']) for x in raw_data["Time Series (Daily)"]]
        ])
        return adjusted_price
    
