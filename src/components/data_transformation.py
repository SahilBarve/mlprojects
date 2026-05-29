import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer# It is used to apply different transformations to different columns of the dataset
from sklearn.impute import SimpleImputer# It is used to fill the missing values in the dataset
from sklearn.pipeline import Pipeline# It is used to create a pipeline of transformations and model training
from sklearn.preprocessing import OneHotEncoder,StandardScaler# It is used to convert categorical variables into numerical variables

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object # We use this when we have defined a function in utils and we want to use them in our current module
@dataclass
class DataTransformationConfig:
  preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')#We created a pickle file here 

class DataTransformation:
  def __init__(self):
    self.data_transformation_config=DataTransformationConfig()#Creates an object of DataTransformationConfig,Stores that object inside the current class object using self

  def get_data_transformer_object(self):
    '''This function is responsible for data transformation based on different types of data''' 
    try:
      numeric_columns=[ 'reading_score', 'writing_score'] # Note we havent mentioned math_score as one of the features cause it is our target col 
      categorical_columns= ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
      #We will create a pipeline and we will handle our missing values
      #We use a pipeline in ML to automate and organize multiple preprocessing/training steps into a single flow.
      num_pipeline=Pipeline(#Will run this pipeline on training dataset and will do just transformation on test dataset
        steps=[
          ("imputer",SimpleImputer(strategy="median")),#This handles missing values
          ("scaler",StandardScaler())#This does scaling
        ]
      )
      cat_pipeline=Pipeline(
        steps=[
          ("imputer",SimpleImputer(strategy="most_frequent")),
          ("one_hot_encoder",OneHotEncoder()),
          ("scaler",StandardScaler(with_mean=False))# with_mean=False Do scaling, but do NOT subtract the mean."
        ]
      )
      logging.info(f"Numerical columns:{numeric_columns}")
      logging.info(f"Categorical columns:{categorical_columns}")
      #Till now we did numerical and column transformation and now will combine them using column transformation
      preprocessor=ColumnTransformer(
        [
          ("num_pipeline",num_pipeline,numeric_columns),#("pipeline name",what pipeline it is,columns )
          ("cat_pipeine",cat_pipeline,categorical_columns)
        ]
      )
      return preprocessor
    except Exception as e:
      raise CustomException(e,sys)
  
  def initiate_data_transformation(self,train_path,test_path):
    try:
      train_df=pd.read_csv(train_path)
      test_df=pd.read_csv(test_path)
      logging.info("Read traina and test data completed")

      logging.info("Obtaining preprocessing object ")

      preprocessing_obj=self.get_data_transformer_object()
      target_column_name="math_score"
      numerical_columns=["writing_score","reading_score"]

      input_feature_train_df=train_df.drop(columns=[target_column_name])# Here we already wrote columns= and now we dont need to specify again like axis=1 drop it
      target_feature_train_df=train_df[target_column_name]

      input_feature_test_df=test_df.drop(columns=[target_column_name])
      target_feature_test_df=test_df[target_column_name]

      logging.info(f"Applying preprocessing object on Training dataframe and Testing dataframe")
      
      input_feature_train_arr=preprocessing_obj.fit_transform( input_feature_train_df)#fit()->learns/calculates something from the data
      input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)#transform()->Applies that learned information to modify the data

      train_arr=np.c_[# np.c_ is a shortcut in NumPy used to combine arrays column-wise.It is commonly used to concatenate arrays horizontally.
        input_feature_train_arr,np.array(target_feature_train_df)#We do so cause Many ML project structures return: complete training array ,complete testing array from the transformation component. so they combine x+y in one same array
      ]
      test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

      logging.info(f"Saved preprocessing object.")
      
      save_object(# we will define this function in utils.py file cause utils.py file contains all the common functionalites that the entire project can use 
        file_path=self.data_transformation_config.preprocessor_obj_file_path,
        obj=preprocessing_obj
      )
      
      return(
        train_arr,
        test_arr,
        self.data_transformation_config.preprocessor_obj_file_path,#preprocessing file pickle path

      )

    except Exception as e :
      raise CustomException(e,sys)



















'''Feature Enginnering means creating new features for example total_score=maths_score+english-score and so '''
#Our dataset has features of various types like numeric and categorical so we need to perform data transformation on them
# We also need to do feature engineering , and we do it here in data transformation
