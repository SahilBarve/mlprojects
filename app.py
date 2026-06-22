from flask import Flask, request, render_template # request for working with the up coming requests
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application=Flask(__name__)#creates a Flask app object named application.__name__ is used to tell application that the app starts from this pyton file and use this location as root of the project file

app=application

##Route for a home
@app.route('/') # Its a route decorator in flask , When someone visits  the URL(/) , run  the function below
def index():
  return render_template('index.html') # render_template() is used to display an HTML page from your Flask application.and this line "Open the index.html file from the templates folder and send it to the user's browser."

@app.route('/predictdata',methods=['GET','POST']) #GET method is used to request or retrive data from the server
                                                  #POST is used to send data to the server
def predict_datapoint():# Will do everything here
  if request.method=='GET': # In GET will just show the input to user and POST will recieve the user input make the prediction and return the result
    return render_template('home.html') # in home.html will have simple data fields that we need to provide to model to do the predictions
  else:
    data=CustomData(
      gender=request.form.get('gender'), # We will get all our input data entered by user here
      race_ethnicity=request.form.get('race_ethnicity'),
      parental_level_of_education=request.form.get('parental_level_of_education'),
      lunch=request.form.get('lunch'),
      test_preparation_course=request.form.get('test_preparation_course'),
      reading_score=float(request.form.get('reading_score')),
      writing_score=float(request.form.get('writing_score'))
    )  # This same class will be created in predict pipeline file and this class is responsilble for mapping all the input data that we are giving to html which will be mapped with the backend 
    pred_df=data.get_data_as_data_frame()
    print(pred_df)

    predict_pipeline=PredictPipeline()
    results=predict_pipeline.predict(pred_df) # Not the predict() always returns a array/list like object so we return results[0]
    return render_template('home.html',results=results[0]) # We returned results[0] cause everything will be in a list format 
  
# For running the code

if __name__=='__main__':  # "Run the code below only if this file is executed directly." This prevents Flask from starting automatically when the file is imported somewhere else.
  app.run(host="0.0.0.0",debug=True) # app.run() starts the flask web server and listens for requests such as http://127.0.0.1:5000 and executes your routes
                                     # host="0.0.0.0." means other devices not only this on the same network can access it without this only the local device can access it

''' Run the file by python app.py then open the crome and type 127.0.0.1:5000/ this will open the home page 
then call the function predictdata by simply writing  127.0.0.1:5000/predictdata in the search bar'''