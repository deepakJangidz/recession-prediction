print("hello deepak")
import uvicorn
from fastapi import FastAPI
import pandas as pd
import pickle

# pickle_in = open('prediction.pkl' , 'wb')
# predict = pickle.load(pickle_in)

import pickle
import os

filepath = "prediction.pkl"  # Replace with your actual file path

if os.path.exists(filepath):
    with open(filepath, 'rb') as pickle_in:
        try:
            predict = pickle.load(pickle_in)
            # Use the loaded data here
        except pickle.UnpicklingError:
            print("Error: Could not unpickle data. File might be corrupted.")
else:
    print("Error: File not found at", filepath)

app.FastAPI()

@app.post('/Predict')
def predict_gdp(data: GDP_Parameter):
    data = data.dict()
    GDP_In_Billion_USD = data['GDP_In_Billion_USD']
    Per_Capita_in_USD = data['Per_Capita_in_USD']
    Percentage_Growth = data['Percentage_Growth']

    prediction = predict.predict([[GDP_In_Billion_USD , Per_Capita_in_USD , Percentage_Growth]])
    return { 'Predicted GDP ' : prediction}