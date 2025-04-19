import requests, pandas as pd
from datetime import datetime, timedelta

def fetch_reddit_posts(subreddit='wallstreetbets', days=7):
    end = int(datetime.utcnow().timestamp())
    start = int((datetime.utcnow() - timedelta(days=days)).timestamp())
    url = 'https://api.pushshift.io/reddit/search/submission'
    params = {'subreddit': subreddit, 'after': start, 'before': end, 'size': 500, 'fields': ['title', 'selftext', 'created_utc']}
    res = requests.get(url, params=params).json()['data']
    df = pd.DataFrame(res)
    df['text'] = df['title'] + ' ' + df['selftext']
    df['date'] = pd.to_datetime(df['created_utc'], unit='s').dt.date
    return df[['date', 'text']]