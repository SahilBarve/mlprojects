import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation # We call this after we have successfully done the data transformation part 
from src.components.data_transformation import DataTransformationConfig# Same with this its use for data-transformation_configuration

from src.components.model_trainer import ModelTrainerConfig# Used for testing the model we trained in model_trainer
from src.components.model_trainer import ModelTrainer



@dataclass# this class is a dataclass and it will automatically generate __init__ and __repr__ functions for us
class DataIngestionConfig:
  train_data_path: str=os.path.join('artifacts',"train.csv")
  test_data_path: str=os.path.join('artifacts',"test.csv")
  raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:# Here we dont use @dataclass cause we dont just need variables 
  def __init__(self):
    self.ingestion_config=DataIngestionConfig()

  def initiate_data_ingestion(self):
    logging.info("Entered the data ingestion method or component")
    try:

      df=pd.read_csv('notebook\data\stud.csv')# Here we took data from a raw csv file but instead of this we could also take data from APIs and Databases like mongodb

      logging.info('Read the dataset as dataframe')

      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

      df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)#header is True by default as well

      logging.info("Train Test Split initiated")
      train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

      logging.info("Ingestion of data is completed")
      
      return(
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )
    except Exception as e:
      raise CustomException(e,sys)
if __name__=="__main__":
  obj=DataIngestion()
  train_data,test_data=obj.initiate_data_ingestion()# Earlier before data transformation we did this i.e we initiate a object for data ingestion obj.initiate_data_ingestion()  
#obj.initiate_data_ingestion() this function returns train and test data path Those paths usually point to the files created/extracted during the data ingestion step.
# Now we will call all the data transformation functions here in the data ingestion file
  data_transformation=DataTransformation()
  train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

modelTrainer=ModelTrainer()
print(modelTrainer.initiate_model_trainer(train_arr,test_arr))


'''Here we basically combined data ingetion and then data transformation (from that __name__ statement)'''
#Data ingestion = taking data from different sources and bringing it into a system.
# In data ingestion we will take data from various data sources like  various databases (like mongodb),hadoop and read it from them 
# Dataclasses is used here for creating class variables 
''' We create DataingestionConfig class to save all the input data , raw data train test  data and all so anything we 
require in data ingestion part we will use it through this DataIngestionConfig class, Output on the
other hand can be anything like numpy,clean and raw  file in a folder '''

'''Example:
Suppose an e-commerce company collects:customer orders,website clicks,payment logs
After ingestion, the output may be: Files in Apache Hadoop HDFS  '''

#__init__ function is used for creating the class attributes and __repr__ function is used for string representation of an object.
'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student(name={self.name}, marks={self.marks})"'''

#pass statements is used as ignore i.e whenever we write pass the program ignores and continues
'''@dataclass is a decorator in Python provided by dataclasses that automatically creates common class methods for you.like(__init__(),__repr__(),__eq__())
If we just want to define class variables then use dataclass or else go with normal class like by using __init__ and all that functions'''
#An artifacts folder is a directory used to store files generated during development, building, testing, or deployment of software.
# And the ('artifacts',test.csv) here test.csv is filename for our artifacts folder for test data and now the test data will be stored in this path

# os.path.dirname() is used return directory part of the filename like  "Home/Doc/Desktop and all
# exists_ok=True means if the folder is already there dont delete and recreate it just keep it as it is.
# "to_csv()" is used in pandas to save data from a DataFrame into a CSV file.
#logging.info() here .info is  a method/function in python used for inserting information in the log 
#index=False means dont consider index while saving the dataframe in to_csv() and header=True means consider columns while saving the dataframe
'''if __name__ == "__main__": we use this in python to check whether a python file is being run directly or imported as
 a module if we are currently in that same directory it will run directly and we are importing that file in the current file it wont run directly'''