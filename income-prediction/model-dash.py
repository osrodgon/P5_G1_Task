from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import requests

# URL of your FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict/revenue"

# Initialize the Dash app
app = Dash(__name__)

# Define the layout using HTML components
app.layout = html.Div(children=[
    html.H1(children="💰 Revenue Prediction App", style={'textAlign': 'center'}),
    html.P(children="Enter the price and day to get a revenue prediction from the FastAPI model.", style={'textAlign': 'center'}),

    html.Div(className="row", children=[
        html.Div(className="col-6", children=[
            html.Img(src="assets/aile.png", style={'height':'300px', 'width':'auto'}),
            html.P("Our Supplements", style={'textAlign': 'center'})
        ]),
        html.Div(className="col-6", children=[
            html.H3("Input Data"),
            html.Div(children="Price ($)", style={'marginBottom': '10px'}),
            dcc.Slider(
                id='price-input',
                min=0,
                max=75,
                value=25,
                step=1
            ),
            html.Div(children="Day of Month", style={'marginTop': '20px', 'marginBottom': '10px'}),
            dcc.Slider(
                id='day-input',
                min=1,
                max=31,
                value=1,
                step=1
            )
        ])
    ], style={'display': 'flex'}),
    
    html.Button("Predict", id="predict-button", n_clicks=0),
    html.Div(id='output-text', style={'marginTop': '20px'})
])

# Define the callback to handle the prediction
@app.callback(
    Output('output-text', 'children'),
    Input('predict-button', 'n_clicks'),
    Input('price-input', 'value'),
    Input('day-input', 'value')
)
def predict_revenue(n_clicks, price, day):
    if n_clicks > 0:
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
    return ""

# Run the app
if __name__ == '__main__':
    app.run(debug=True)