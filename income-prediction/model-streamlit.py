import streamlit as st
import requests

# URL of your FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict/revenue"

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Revenue Prediction App",
    page_icon="💰",
    layout="centered"
)

# App title and description
st.title("💰 Revenue Prediction App")
st.markdown("Enter the price and day to get a revenue prediction from the FastAPI model.")

# Create two columns for the image and input data
col1, col2 = st.columns(2)

# Place the image in the first column
with col1:
    st.image("aile.png", caption="Our Supplements", use_container_width=True)

# Place the input widgets in the second column
with col2:
    st.subheader("Input Data")
    price_input = st.slider("Price ($)", min_value=0, max_value=75, value=25)
    day_input = st.slider("Day of Month", min_value=1, max_value=31, value=1)

# Function to call the FastAPI endpoint
def predict_revenue(price, day):
    """
    Function to call the FastAPI endpoint with user input.
    """
    try:
        data = {
            "Price": price,
            "Day": day
        }
        
        response = requests.post(FASTAPI_URL, json=data)
        response.raise_for_status()
        
        prediction = response.json().get("predicted_revenue")
        
        return f"Predicted Revenue: ${prediction:.2f}"
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the FastAPI. Please ensure it is running."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Prediction button and logic
if st.button("Predict"):
    # Show a spinner while the prediction is in progress
    with st.spinner("Predicting..."):
        # Get the prediction from the FastAPI endpoint
        result = predict_revenue(price_input, day_input)
    
    # Display the result
    st.subheader("Prediction Result")
    st.success(result)