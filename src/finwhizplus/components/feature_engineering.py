import pandas as pd

def add_technical_indicators(df):
    df['RSI'] = df['Close'].rolling(14).mean()
    df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
    return df.dropna()

def merge_with_stock(stock_df, sentiment_df):
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
    return stock_df.merge(sentiment_df, left_on='Date', right_on='date', how='left').fillna(method='ffill')