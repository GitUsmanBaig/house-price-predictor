from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load your trained model
model = joblib.load('house_price_predictor_model.pkl')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)
        print("Received data:", data)  # Log received data
        
        # Convert input data into DataFrame
        input_df = pd.DataFrame([data])
        print("DataFrame:", input_df)  # Log the DataFrame

        # Make prediction
        prediction = model.predict(input_df)[0]  # Get the first prediction

        # Respond with prediction
        return jsonify({'prediction': prediction})
    except Exception as e:
        print("Error:", str(e))  # Log the error
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
