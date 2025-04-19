import tweepy, pandas as pd
from datetime import datetime, timedelta

def get_twitter_client(bearer_token):
    return tweepy.Client(bearer_token=bearer_token)

def fetch_tweets(client, query='$AAPL OR #AAPL', days=7, max_results=100):
    end = datetime.utcnow()
    start = end - timedelta(days=days)
    tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'text'],
        start_time=start.isoformat('T') + 'Z', end_time=end.isoformat('T') + 'Z', max_results=max_results)
    return pd.DataFrame([{'date': t.created_at.date(), 'text': t.text} for t in tweets.data])