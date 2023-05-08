from datareader import Reader
import numpy as np

TICKERS = ['meta', 'appl', 'msft', 'amzn', 'tsla', 'v', 'goog','jpm', 'NVDA', 'UNH']
for i,t in enumerate(TICKERS):
    r = Reader(t)
    data = r.get_all_data()
    data.tofile(f'{i}.csv', sep = ',')
    