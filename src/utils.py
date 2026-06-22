import os
import sys

import numpy as np
import pandas as pd
import dill # Used in saving a pickle file
from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
  try:
    dir_path=os.path.dirname(file_path)

    os.makedirs(dir_path,exist_ok=True)
    # file_obj is just a variable name that refers to the opened file.
    with open(file_path,"wb")as file_obj:# This is used to open the file and then close the file once the work is done no need to write file_obj.close()
      dill.dump(obj,file_obj)#dill is similar to pickle but more powerful.
  except Exception as e:
    raise CustomException(e,sys)

def evaluate_model(X_train, y_train, X_test, y_test, models,param):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)#In Python, ** is used to unpack a dictionary into keyword arguments. all the things in the best_params are feed to model as argument parameters
            model.fit(X_train,y_train)
            # Train model
            #model.fit(X_train,y_train)

            # Predict Training data
            y_train_pred = model.predict(X_train)

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score
        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
   try:
      with open(file_path,"rb")as file_obj:
         return dill.load(file_obj)
   except Exception as e:
      raise CustomException(e,sys)