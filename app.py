# Filename: app.py

from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Check if the model file exists
model_file = 'model.pkl'
if os.path.exists(model_file):
    model = joblib.load(model_file)
else:
    model = None
    print("Model file not found. Please train the model by running main.py.")

@app.route('/predict', methods=['POST'])
def predict():
    if model is not None:
        try:
            data = request.get_json()
            features = data['features']
            prediction = model.predict([features])
            return jsonify({'prediction': list(prediction)})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Model not loaded. Please train the model and try again.'})

if __name__ == '__main__':
    app.run(debug=True)
