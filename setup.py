from setuptools import setup, find_packages

setup(
    name='finwhiz',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask', 'pandas', 'scikit-learn', 'yfinance',
        'nltk', 'transformers', 'torch', 'joblib', 'matplotlib', 'seaborn',
        'tweepy', 'requests'
    ],
)