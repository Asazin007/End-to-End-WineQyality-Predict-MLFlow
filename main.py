from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.pipelines.stage_01_data_ingestion import DataIngestionTraningPipeline
import sys
from src.ml_project.pipelines.stage_02_data_validation import DataValidationTraningPipeline
from src.ml_project.pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.ml_project.pipelines.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.ml_project.pipelines.stage_05_model_evaluation import ModelEvaluationTraningPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTraningPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
    logging.info("Custom Exeption")
    raise CustomException(e, sys)



STAGE_NAME = "Data Validation Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTraningPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
    logging.info("Custom Exeption")
    raise CustomException(e, sys)




STAGE_NAME = "Data Transformation Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise CustomException(e, sys)

STAGE_NAME = "Model Trainer Stage"



try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise CustomException(e, sys)



STAGE_NAME ="Model Evaluation Stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationTraningPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise CustomException(e,sys)
