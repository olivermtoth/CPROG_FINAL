from datareader import Reader
import numpy as np
from time import sleep

TICKERS = [
    'aapl', 'msft', 'amzn', 'nvda', 'googl', 'brk.b','meta', 'tsla', 'unh', 'xom',
    'jnj', 'mrk', 'hd', 'cvx', 'pep', 'avgo', 'abbv',
    'ko', 'cost', 'mcd','pfe', 'wmt', 'tmo', 'crm', 'abt','bac', 'csco', 'dis', 'lin',
    'cmcsa', 'acn', 'vz', 'nke', 'adbe'
    ]

for i,t in enumerate(TICKERS):
    r = Reader(t)
    data = r.get_all_data()
    data.to_csv(f'data/{t}.csv', sep = ',', index=True)
    print(f'{i+1}/{len(TICKERS)},  {t.capitalize()}: DONE')
    sleep(10)
