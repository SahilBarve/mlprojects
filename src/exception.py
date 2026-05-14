# Will write all the exceptions here
import sys
from src.logger import logging
'''The Python sys module provides access to variables and functions that interact closely with the Python interpreter 
and runtime environment'''

def error_message_detail(error,error_detail:sys):
  _,_,exc_tb=error_detail.exc_info()
  file_name=exc_tb.tb_frame.f_code.co_filename 
  error_message=("Error occured in python script name [{0}] line number [{1}] error messsage[{2}]").format(
    file_name,exc_tb.tb_lineno,str(error)
   )
  return error_message   

  # error_detail:sys means error detail should contain sys module
  # exc_info will tell all the info about the error that we get,# exc_info() returns exception type, value, and traceback
  #by this "exc_tb.tb_frame.f_code.co_filename" code we will get the file in which error has occured
  # exc_tb is a traceback object that stores information about where the error occurred
  # we will write all the parameters that will take the placeholders place like name[{0}] will be file_name and same for the rest two 

class CustomException(Exception):
  def __init__(self,error_message,error_detail:sys):
    super().__init__(error_message)
    self.error_message=error_message_detail(error_message,error_detail=error_detail)
  
  def __str__(self):
    return self.error_message 

  #__init__ is a constructor in Python classes.It is a special function that automatically runs when an object is created.
  #""""Exception is a inbuild python class for errors """"
  # class CustomException(Exception) -> inherits from Exception class
  # super().__init__(error_message)-> calls the parent Exception class constructor and passes error_message as parameter
  #self is the current object of the class.
  # when we print the def __str__ will get the error message, __str__ is a special method used to define:how an object should look when converted to a string.
 
'''If we simply print the object's  error_message without using __str__ class will get something like this
 <__main__.Student object at 0x000001F...>
cause  Python does NOT know: how you want the object to be shown,So it prints the default object information.
and whenever we use this __str__ function it prints the object attribute that is error_message in  our case'''
 
# so now whenever in cache block we raise custom exception this message will popup that is what is the filename
# where exception occured , at what line it occured and it will display the error message along with the error

#We use the main functio for checking if the file is working or not
'''
if __name__=="__main__" :# used to just see if everything is working fine or not
  try:
    a=1/0
  except Exception as e:
    logging.info("Divide by Zero")
    raise CustomException(e,sys)
'''
# For running this use command python -m  src.excption in terminal and it will display an Divide by Zero error message

