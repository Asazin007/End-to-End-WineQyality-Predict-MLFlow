from src.ml_project.config.configuration import configurationManager
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
import sys

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTraningPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
    
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage{STAGE_NAME} started <<<<<<")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logging.info(f">>>>>> stage{STAGE_NAME} completed <<<<<<\n\nX=========X")
    except Exception as e:
            logging.info("Custom Exeption")
            raise CustomException(e,sys)

