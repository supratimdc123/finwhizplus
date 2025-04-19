import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def clean_and_score(news_df):
    sia = SentimentIntensityAnalyzer()
    news_df['combined'] = news_df.iloc[:, 2:27].apply(lambda row: ' '.join(str(val) for val in row), axis=1)
    news_df['sentiment'] = news_df['combined'].apply(lambda x: sia.polarity_scores(x)['compound'])
    news_df['Date'] = pd.to_datetime(news_df['Date'])
    return news_df[['Date', 'sentiment']]
