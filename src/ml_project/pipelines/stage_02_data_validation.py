from src.ml_project.config.configuration import configurationManager
from src.ml_project.components.data_validation import DataValiadtion
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys


STAGE_NAME = "Data Validation Stage"

class DataValidationTraningPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):    
        config = configurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
        

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTraningPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
    except Exception as e:
            logging.info("Custom Exeption")
            raise CustomException(e,sys)
