"""
Getting data via https://www.alphavantage.co/ API
"""
import json
import requests



class Reader():

    def __init__(self, ticker, time_frame, datatype='json'):
        with open('API_KEY', 'r', encoding='utf-8') as f:
            self.apikey = f.readline()
        self.ticker = ticker
        if time_frame.lower() not in ['1min', '5min', '15min', '30min', '60min', '1d']:
            raise InvalidTimeFrameError(f"{time_frame} is not an avialable timeframe.")


    def getdata(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&apikey={self.apikey}'
        data = requests.get(url,timeout=5).json()
        return data

        
class InvalidTimeFrameError(Exception):
    pass
