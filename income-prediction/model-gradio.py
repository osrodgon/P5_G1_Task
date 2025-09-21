import gradio as gr
import requests

# URL of your FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict/revenue"

def predict_revenue(price, day):
    """
    Function to call the FastAPI endpoint with user input.
    """
    try:
        # Prepare the data as a dictionary
        data = {
            "Price": price,
            "Day": day
        }
        
        # Make the POST request to the FastAPI endpoint
        response = requests.post(FASTAPI_URL, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        # Parse the JSON response
        prediction = response.json().get("predicted_revenue")
        
        return f"Predicted Revenue: ${prediction:.2f}"
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the FastAPI. Please ensure it is running."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Create the Gradio interface
# We use a 'Blocks' layout for more control over the UI
with gr.Blocks() as demo:
    gr.Markdown("# Revenue Prediction App")
    gr.Markdown("Enter the price and day to get a revenue prediction from the FastAPI model.")
    
    with gr.Row():
        gr.Image("aile.png", 
                 label="Our Supplements",
                 height=300)
        with gr.Column():
            price_input = gr.Slider(minimum=0, maximum=75, label="Price ($)")
            day_input = gr.Slider(minimum=1, maximum=31, step=1, label="Day of Year")
    
    predict_button = gr.Button("Predict")
    
    output_text = gr.Textbox(label="Prediction Result")
    
    # Define the action when the button is clicked
    predict_button.click(
        fn=predict_revenue,
        inputs=[price_input, day_input],
        outputs=output_text
    )

# Launch the Gradio app
demo.launch()
