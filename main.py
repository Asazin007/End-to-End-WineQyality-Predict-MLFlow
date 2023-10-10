from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.pipelines.stage_01_data_ingestion import DataIngestionTraningPipeline
import sys

STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>> stage{STAGE_NAME} started <<<<<<")
    obj = DataIngestionTraningPipeline()
    obj.main()
    logging.info(f">>>>>> stage{STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
    logging.info("Custom Exeption")
    raise CustomException(e,sys)