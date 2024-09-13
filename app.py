from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load('house_price_predictor_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from Post request
        data = request.get_json()
        
        # Convert input data into DataFrame
        input_df = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(input_df)[0]  # [0] to get the single value
        
        # Respond with prediction
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
