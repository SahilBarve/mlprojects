'''We create this pipeline for  creating a web application that will interact with the pickle files , 
it will take input data and then will interact with the pickle files and return us the final result.
till now we did the whole data ingestion, transformation and model training part its the next step in the pipeline'''
# We will create a app.py file for creating application , we are using flask for creating application

import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object # load object  function is responsible opening the file in read mode and loading the pickle file by using the dill

class PredictPipeline:
  def __init__(self):
    pass

  def predict(self,features):
   try:
      model_path='artifacts\model.pkl'
      preprocessor_path='artifacts\preprocessor.pkl'
      model=load_object(file_path=model_path)
      preprocessor=load_object(file_path=preprocessor_path)
      data_scaled=preprocessor.transform(features)
      preds=model.predict(data_scaled)
      return preds
   
   except Exception as e:
     raise CustomException(e,sys)
  

class CustomData:# The Same CustomData class that we created in app.py file will be created here in this file
  def __init__(
      self,
      gender:str,
      race_ethnicity:str,
      parental_level_of_education,
      lunch:str,
      test_preparation_course:str,
      reading_score:int,
      writing_score:int
  ):
     self.gender=gender

     self.race_ethnicity=race_ethnicity

     self.parental_level_of_education=parental_level_of_education

     self.lunch=lunch

     self.test_preparation_course=test_preparation_course

     self.reading_score=reading_score

     self.writing_score=writing_score
     
  def get_data_as_data_frame(self):
     try:
       custom_data_input_dict={ # For converting data into a dataframe we created a dictionary from that data and will create a dataframe of the dictionary
          "gender":[self.gender],
          "race_ethnicity":[self.race_ethnicity],
          "parental_level_of_education":[self.parental_level_of_education],
          "lunch":[self.lunch],
          "test_preparation_course":[self.test_preparation_course],
          "reading_score":[self.reading_score],
          "writing_score":[self.writing_score]
       }

       return pd.DataFrame(custom_data_input_dict)
     except Exception as e:
       raise CustomException(e,sys)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     '''
User enters data
        ↓
Flask receives data
        ↓
CustomData class creates DataFrame
        ↓
PredictPipeline loads model.pkl
        ↓
PredictPipeline loads preprocessor.pkl
        ↓
Transform data
        ↓
Predict score
        ↓
Return result to Flask
        ↓
Display prediction on home.html
'''

'''PredictPipeline exists to encapsulate all prediction-related logic (loading artifacts, preprocessing, and predicting)
 in one place, keeping your Flask code clean and organized.'''