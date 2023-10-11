from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.pipelines.stage_01_data_ingestion import DataIngestionTraningPipeline
import sys
from src.ml_project.pipelines.stage_02_data_validation import DataValidationTraningPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTraningPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
    logging.info("Custom Exeption")
    raise CustomException(e,sys)


STAGE_NAME = "Data Validation Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTraningPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
    logging.info("Custom Exeption")
    raise CustomException(e,sys)