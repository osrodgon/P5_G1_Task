import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Load the pre-trained model and scaler
try:
    model = joblib.load("model_lasso.joblib")
    scaler = joblib.load("standard_scaler.joblib")
except FileNotFoundError:
    raise RuntimeError("Model or scaler not found. Please ensure 'model.joblib' and 'scaler.joblib' exist.")

# 2. Initialize the FastAPI app
app = FastAPI()

# 3. Define the input data structure using Pydantic
class InputData(BaseModel):
    Price: float
    Day: float

# 4. Create the prediction endpoint
@app.post("/predict/revenue")
def predict_revenue(data: InputData):
    """
    Predicts revenue based on Price and Day.
    """
    # Create a DataFrame from the input data
    # The column names MUST match the names used during training.
    input_df = pd.DataFrame([[data.Price, data.Day]],
                            columns=["Price", "Day"])

    # Scale the input data using the pre-trained scaler
    scaled_input = scaler.transform(input_df)

    # Make the prediction using the loaded model
    prediction = model.predict(scaled_input)

    # Return the prediction as a JSON object
    return {"predicted_revenue": prediction[0]}