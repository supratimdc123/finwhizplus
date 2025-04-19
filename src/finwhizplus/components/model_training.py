import joblib, os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(df):
    X = df[['sentiment_score', 'RSI', 'MACD']]
    y = (df['Close'].shift(-1) > df['Close']).astype(int)[:-1]
    X = X[:-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    os.makedirs('artifacts', exist_ok=True)
    joblib.dump(model, 'artifacts/model.pkl')