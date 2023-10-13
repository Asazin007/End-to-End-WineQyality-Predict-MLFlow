from src.ml_project.config.configuration import configurationManager
from src.ml_project.components.model_evaluation import ModelEvaluation
from src.ml_project.logger import logging
import sys
from src.ml_project.exception import CustomException

STAGE_NAME ="Model Evaluation Stage"


class ModelEvaluationTraningPipeline:
    def __init__(self) -> None:
        pass
    
    
    def main(self):
        config = configurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        
        

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTraningPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)
