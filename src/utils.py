import os
import sys
import numpy as np
import pandas as pd
import pickle
from src.exception import CustomException
from src.logger import logging



def save_object(file_path, obj):
    """
    Save the object to a file using pickle.
    """
    logging.info(f"Saving object to {file_path}")
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved to {file_path}")
    except Exception as e:
        raise CustomException(e, sys)