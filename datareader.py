"""
Getting data via https://www.alphavantage.co/ API for stock prices
and https://finnhub.io/ for other finacial data and indicators.
"""
import requests
import numpy as np
import pandas as pd
import ta
# TODO: Finish rsi


class Reader():

    def __init__(self, ticker):
        """
        Initalizing Reader object to acsess market data.
        """
        with open('API_KEY', 'r', encoding='utf-8') as f:
            self.apikey = f.readline()
            f.close()
        self.ticker = ticker
    
    def get_100days_data(self):
        """
        Get data from the last 100 day
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&apikey={self.apikey}'
        raw_data = requests.get(url,timeout=5).json()
        data = pd.DataFrame.from_dict(raw_data["Time Series (Daily)"]).T
        data = data.iloc[::-1]
        res = pd.DataFrame()
        res['prices'] = data['5. adjusted close']
        res['volume'] = data['6. volume']
        # res['rsi'] = ta.momentum.RSIIndicator(data['5. adjusted close']).rsi()
        res['macd'] = ta.trend.MACD(data['5. adjusted close']).macd()
        res = res.iloc[::-1]
        return res
    
    def get_all_data(self):
        """
        Get the full available historical price
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&outputsize=full&apikey={self.apikey}'
        raw_data = requests.get(url,timeout=5).json()
        data = pd.DataFrame.from_dict(raw_data["Time Series (Daily)"]).T
        data = data.iloc[::-1]
        res = pd.DataFrame()
        res['prices'] = data['5. adjusted close']
        res['volume'] = data['6. volume']
        # res['rsi'] = ta.momentum.RSIIndicator(data['5. adjusted close']).rsi()
        res['macd'] = ta.trend.MACD(data['5. adjusted close']).macd()
        res = res.iloc[::-1]
        return res