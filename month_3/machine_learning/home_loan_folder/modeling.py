from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# load the saved model
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

#let's initialize our application
app = FastAPI()

#lets create our pydantic model
class HomeLoanFeatures(BaseModel):
    Gender: object
    Married: object
    Dependents: object
    Education : object
    Self_Employed: object
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    property_Area: float
    
#let's create our endpoints
@app.get('/')
def home():
    return {"message": "Welcome to Home Loan App Predictor"}

# prediction endpoint
# convert the features to 2d numpy array using [[]]

@app.post('/predict')
def predict(Status: HomeLoanFeatures):
    features = np.array([[
        Status.Gender,
        Status.Married,
        Status.Dependents,
        Status.Education,
        Status.Self_Employed,
        Status.ApplicantIncome,
        Status.CoapplicantIncome,
        Status.LoanAmount,
        Status.Loan_Amount_Term,
        Status.Credit_History,
        Status.property_Area
    ]])


    # let's scale our input features using the loaded scaler( to  normalize the input)
    scaled_features = scaler.transform(features)
    
    # let's make prediction with the loaded model
    prediction = model.predict(scaled_features)
    
    # return the predicted result and the convert the prediction to string for serialization
    
    return {"predicted_status": str(prediction[0])}

# let's run our prediction app
# run with ---uvicorn wine_app:app --reload
