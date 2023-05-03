"""
Getting data via https://www.alphavantage.co/ API
"""
import csv
import requests



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
        data = requests.get(url,timeout=5)
        return data


