from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('path_to_your_model/house_price_predictor_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from Post request
        data = request.get_json()
        # Assuming data is passed as a list of values
        features = [data['area'], data['bedrooms'], data['bathrooms'], data['stories'],
                    data['mainroad'], data['guestroom'], data['basement'],
                    data['hotwaterheating'], data['airconditioning'], data['parking'],
                    data['prefarea'], data['furnishingstatus']]
        
        # Make prediction
        prediction = model.predict([features])[0]  # [0] to get the single value
        
        # Respond with prediction
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
