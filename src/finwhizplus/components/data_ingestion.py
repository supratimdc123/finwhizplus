import yfinance as yf
import pandas as pd

def get_stock_data(ticker='AAPL', period='1y'):
    df = yf.download(ticker, period=period)
    df.to_csv('data/stock.csv')
    return df