#A logger file is created to: store information about what your program is doing while it runs.
# The file records what happened,when happended and why it failed
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"log",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# f string is a modern way in python to insert variables in string , .log is a file extension used for log file
# getcwd-> This stands for current working directory and "log" simply  will be displayed befor LOG_FILE
#exist_ok =True means keep on appending the new files even when we already have a folder 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
  level=logging.INFO,
)
# level=logging.INFO,This will helps us control how much information gets printed.

'''Now whenever we use logging.INFo we will get the configuration in terms of this above given logging
basic.Confi function'''

'''So now we have already created the logging and exception file so whenever an exceptions comes we will 
logging it with our logger file and use logging.INFO to put it in our file so such a way will be able to 
get that folder also'''
 '
 '''
if __name__=="__main__" :# used to just see if everything is working fine or not
  logging.info("Logging has started")
'''
# For checking if the logger.py file got created successfully we run the command python src/looger.py
# and if a log file is created in our project file we know it is created succesfully and the file that is created will be in same format as we mentioned above