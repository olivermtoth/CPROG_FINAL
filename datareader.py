"""
Getting data via https://www.alphavantage.co/ API
"""
import requests
from datetime import date, timedelta
import pandas



class Reader():

    def __init__(self, ticker):
        """
        Initalizing Reader object to acsess market data.
        """
        with open('API_KEY', 'r', encoding='utf-8') as f:
            self.apikey = f.readline()
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
        data = requests.get(url,timeout=5).json()
        return data
    
    def get_all_data(self):
        """
        Get the full available historical price
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&outputsize=full&apikey={self.apikey}'
        data = requests.get(url,timeout=5).json()
        return data



