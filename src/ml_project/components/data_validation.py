import os
import pandas as pd
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema_cols =self.config.all_schema
            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break  # No need to continue checking if one column is invalid
                if data[col].dtype != all_schema_cols[col]:
                    validation_status = False
                    break

            # Write the validation status to the status file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

