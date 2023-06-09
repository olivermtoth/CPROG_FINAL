"""
Getting data via https://www.alphavantage.co/ API for stock prices
and calculating indicators with ta.
"""
import requests
import pandas as pd
import ta
import numpy as np


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
        data = pd.DataFrame.from_dict(raw_data["Time Series (Daily)"], dtype=float).T.iloc[::-1]
        # data['shifted'] = data['5. adjusted close'].shift(20)
        res = pd.DataFrame()
        res['price'] = data['5. adjusted close']
        res['volume'] = data['6. volume']
        res['rsi'] = ta.momentum.RSIIndicator((res['price'])).rsi()
        res['macd'] = ta.trend.MACD(data['5. adjusted close']).macd()
        res['adx'] = ta.trend.ADXIndicator(data['2. high'], data['3. low'], data['4. close'] ).adx()
        res['obv'] = ta.volume.OnBalanceVolumeIndicator(data['5. adjusted close'], data['6. volume']).on_balance_volume()
        # res['target'] = (data['5. adjusted close'] < data['shifted']).astype(int)
        return res.dropna() 
    
    def get_all_data(self, for_chart=False):
        """
        Get the full available historical price
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.ticker}&outputsize=full&apikey={self.apikey}'
        raw_data = requests.get(url,timeout=5).json()["Time Series (Daily)"]
        if for_chart == False:
            data = pd.DataFrame.from_dict(raw_data, dtype=float).T.iloc[::-1]
            # data['shifted'] = data['5. adjusted close'].shift(20)
            res = pd.DataFrame()
            res['price'] = data['5. adjusted close']
            res['volume'] = data['6. volume']
            res['rsi'] = ta.momentum.RSIIndicator((res['price'])).rsi()
            res['macd'] = ta.trend.MACD(data['5. adjusted close']).macd()
            res['adx'] = ta.trend.ADXIndicator(data['2. high'], data['3. low'], data['4. close'] ).adx()
            res['obv'] = ta.volume.OnBalanceVolumeIndicator(data['5. adjusted close'], data['6. volume']).on_balance_volume()
            # res['target'] = (data['5. adjusted close'] < data['shifted']).astype(int)
            return res.dropna()
        elif for_chart == True:
            res =  []
            for date in raw_data.keys():
                res.append({'date':date, 'open':raw_data[date]['1. open'], 'high':raw_data[date]['2. high'], 'low':raw_data[date]['3. low'], 'close':raw_data[date]['4. close']})
            return res[::-1]
        elif for_chart == None:
            #Create array for chart
            chart_data =  []
            for date in raw_data.keys():
                chart_data.append({'date':date, 'open':raw_data[date]['1. open'], 'high':raw_data[date]['2. high'], 'low':raw_data[date]['3. low'], 'close':raw_data[date]['4. close']})
            
            #Create data for prediction
            data = pd.DataFrame.from_dict(raw_data, dtype=float).T.iloc[::-1]
            data['shifted'] = data['5. adjusted close'].shift(20)
            res = pd.DataFrame()
            res['price'] = data['5. adjusted close']
            res['volume'] = data['6. volume']
            res['rsi'] = ta.momentum.RSIIndicator((res['price'])).rsi()
            res['macd'] = ta.trend.MACD(data['5. adjusted close']).macd()
            res['adx'] = ta.trend.ADXIndicator(data['2. high'], data['3. low'], data['4. close'] ).adx()
            res['obv'] = ta.volume.OnBalanceVolumeIndicator(data['5. adjusted close'], data['6. volume']).on_balance_volume()
            res['target'] = (data['5. adjusted close'] < data['shifted']).astype(int)
            return {'chart_data':chart_data, 'prediction_data':res}
            
    def get_current_price(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&symbol={self.ticker}&apikey={self.apikey}'
        raw_data = requests.get(url).json()
        data = pd.DataFrame.from_dict(raw_data["Time Series (1min)"], dtype=float).T
        return data['1. open'].iloc[0]