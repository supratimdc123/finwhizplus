# 🚀 FinWhiz+

FinWhiz+ is a powerful stock forecasting application that uses historical price trends and sentiment analysis from financial news, Reddit posts, and Tweets to predict the next day's stock price movement (Up/Down).

Deployed using **Flask + Azure Web App**, this project demonstrates full-stack machine learning engineering: from data ingestion and preprocessing to model training, prediction, and web deployment.

---

## 📊 Features

- 📈 Stock data ingestion using Yahoo Finance API
- 📰 Sentiment analysis from financial news headlines
- 🐦 Twitter API + Reddit Pushshift integration
- 🧠 Technical indicators like RSI and MACD
- 🧪 Random Forest classifier for binary stock movement prediction
- 🌐 Flask app for interactive prediction display
- ☁️ Azure-ready deployment pipeline
- 🧰 Modular project structure with logging and exception handling

---

## 🛠 Tech Stack

| Category         | Tools Used                                 |
|------------------|---------------------------------------------|
| **Language**     | Python                                      |
| **ML/Stats**     | scikit-learn, Transformers, yFinance        |
| **NLP Models**   | FinBERT, VADER                              |
| **Data**         | News dataset (Kaggle), Reddit, Twitter      |
| **Visualization**| Matplotlib, Seaborn                         |
| **Web Framework**| Flask                                       |
| **Deployment**   | Azure App Service, GitHub Actions (CI/CD)   |

---

## 📁 Project Structure

```plaintext
finwhiz/
├── src/finwhizplus/
│   ├── components/                  # ML logic
│   ├── pipelines/                   # Training / prediction pipelines
│   ├── utils.py                     # Common utilities
│   ├── logger.py                    # Logging setup
│   └── exception.py                 # Custom exception class
├── artifacts/                       # Trained model (model.pkl)
├── data/                            # Local data storage
├── templates/                       # Flask HTML UI
├── app.py                           # Flask application
├── requirements.txt
├── setup.py
└── README.md
```
### CURRENTLY UNDER DEVELOPMENT !!!
