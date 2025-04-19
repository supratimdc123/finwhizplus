import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "finwhizplus"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/feature_engineering.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/predict.py",
    f"src/{project_name}/components/sentiment_analyzer.py",
    f"src/{project_name}/components/reddit_fetcher.py",
    f"src/{project_name}/components/twitter_fetcher.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    "requirements.txt",
    "setup.py",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} already exists")