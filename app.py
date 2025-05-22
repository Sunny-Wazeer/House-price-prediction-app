from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            features = [
                float(request.form['MedInc']),
                float(request.form['HouseAge']),
                float(request.form['AveRooms']),
                float(request.form['AveBedrms']),
                float(request.form['Population']),
                float(request.form['AveOccup']),
                float(request.form['Latitude']),
                float(request.form['Longitude'])
            ]

            input_df = pd.DataFrame([features], columns=[
                'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                'Population', 'AveOccup', 'Latitude', 'Longitude'
            ])

            prediction = model.predict(input_df)[0]
            output = f"${prediction * 100000:.2f}"
            return render_template('index.html', prediction=output)

        except Exception as e:
            return render_template('index.html', prediction="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
