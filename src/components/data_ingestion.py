import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw_data.csv')
    input_data_path: str = os.path.join('notebook', 'data', 'stud.csv')
    random_state: int = 42  # Default random state for reproducibility


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method starts")
        try:
            df = pd.read_csv(self.ingestion_config.input_data_path)
            logging.info("Reading the dataset as dataframe")
            raw_data_dir = os.path.dirname(self.ingestion_config.raw_data_path)
            if not os.path.exists(raw_data_dir):
                logging.info(f"Creating directory: {raw_data_dir}")
                os.makedirs(raw_data_dir, exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)
            train_set, test_set = train_test_split(df, test_size= 0.2, random_state= self.ingestion_config.random_state)
            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df, test_size= 0.2, random_state= 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)

            logging.info("Data Ingestion completed successfully")
        
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Ingestion Script")
    parser.add_argument("--log-level", type=str, default="INFO", help="Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR)")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level.upper())
    logging.info("Starting the Data Ingestion process")

    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    logging.info(f"Data Ingestion completed. Train data saved at: {train_path}, Test data saved at: {test_path}")