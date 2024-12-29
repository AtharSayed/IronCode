import pickle
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model from the correct pickle file
with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the StandardScaler object (to scale user input data the same way as training data)
scaler = StandardScaler()

# Home route to render the input form
@app.route('/')
def home():
    return render_template('index.html')

# Predict route to process user input and show the prediction result
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form (assuming it’s numerical data)
        input_data = [float(request.form[field]) for field in request.form if field != 'submit']

        # Convert the input data to a DataFrame
        input_df = pd.DataFrame([input_data], columns=[f'feature_{i}' for i in range(1, len(input_data) + 1)])

        # Scale the input data
        scaled_input = scaler.fit_transform(input_df)  # You might want to use the same scaler used for training

        # Make the prediction using the trained model
        prediction = model.predict(scaled_input)

        # Return the result to the template
        return render_template('index.html', prediction=prediction[0])

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
