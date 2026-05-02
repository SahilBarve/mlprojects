from setuptools import find_packages,setup  # It will find all the packages that are present in the entire ml directory which are required for bulding the application
from typing import List # This module is used for using List

# whenever we are creating a package we need to write what is the name of project what is the application and all
#That is just all the info about project

''' We require many libraries and we cant put everything in the list like(install_requires=['pandas','numpy','seaborn'])
so we create a function named get_requirements and here will give path of the requirement.txt file cause here
in this txt file will mention all the libraries we require and function will install it one by one '''

def get_requirements(file_path:str)->List[str]: # "file_path:str" this tells that we are taking file path as a string and putiing it in a list
  
  '''this function will return a list of requirements'''
  HYPEN_E_DOT="-e."
  requirements=[]
  with open(file_path)as file_obj:
    '''Here we open the file using filepath as an  file_object '''
    
    requirements=file_obj.readlines()# we readlines inside the file using this readlines function

   # The problem here is when we read from the  file after every libarary or module we get a '/n' i.e a newline charachter
   # This newline charachter also gets read by the function and is then inserted in the list to prevent this we replace it with empty space
  
    requirements=[req.replace("/n","")for req in requirements]
 
    ''' when we are installing all the requirements from requirements.txt file we also want setup.py to build the application parallely
   and for that we write " -e. "in the requirements.txt file cause this will trigger the setup.py file '''
   # But also we dont want to read the "-e." in our requirements list so we will remove it from the requirements list
    if HYPEN_E_DOT in requirements:
     requirements.remove(HYPEN_E_DOT)
  return requirements


setup(
name='mlproject',
version='0.0.1',
author='Sahil',
author_email='Sahilbarve1000@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)


''' for setup file to find all the packages we create a seprate file named src and if we 
want src file to be fpund as a package we create a __init__.py file in it 
and once we do it whenver this find-packages is running it will go and see in how many folders we have 
this __init__ file and will directly consider this src as package itself
And then it will try to build it and we could import it and use it whever we want
'''

