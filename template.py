import os 
from pathlib import Path
import logging


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/WineQualityPrediction/components/__init__.py",
    f"src/WineQualityPrediction/components/data_ingestion.py",
    f"src/WineQualityPrediction/components/data_transformation.py",
    f"src/WineQualityPrediction/components/model_trainer.py",
    f"src/WineQualityPrediction/components/model_evaluation.py",
    f"src/WineQualityPrediction/components/model_monitering.py",
    f"src/WineQualityPrediction/pipelines/__init__.py",
    f"src/WineQualityPrediction/pipelines/training_pipeline.py",
    f"src/WineQualityPrediction/pipelines/prediction_pipeline.py",
    f"src/WineQualityPrediction/exception/exception.py",
    f"src/WineQualityPrediction/logger/logging.py",
    f"src/WineQualityPrediction/logger/logs/",
    f"src/WineQualityPrediction/util/__init__.py",
    f"src/WineQualityPrediction/util/utils.py",
    f"deployment/docker/Dockerfile",
    f"deployment/docker/docker-compose.yaml",
    f"deployment/docker/requirements.txt",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb",
    f"data/"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")