from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def score_sentiment(df, text_col='text'):
    df['sentiment_score'] = df[text_col].apply(
        lambda x: sentiment_model(x[:512])[0]['score'] * (1 if sentiment_model(x[:512])[0]['label'] == 'POSITIVE' else -1)
    )
    return df