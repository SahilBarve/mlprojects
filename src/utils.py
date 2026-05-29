import os
import sys

import numpy as np
import pandas as pd
import dill # Used in saving apickle file

from src.exception import CustomException

def save_object(file_path,obj):
  try:
    dir_path=os.path.dirname(file_path)

    os.makedirs(dir_path,exist_ok=True)

    with open(file_path,"wb")as file_obj:# This is used to open the file and then close the file once the work is done no need to write file_obj.close()
      dill.dump(obj,file_obj)#dill is similar to pickle but more powerful.
  except Exception as e:
    raise CustomException(e,sys)

