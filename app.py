from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)
model_path = 'model.pkl'

if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("Model loaded successfully")
else:
    model = None
    print("Failed to load model")

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            data = request.get_json()
            prediction = model.predict([data['features']])
            return jsonify({'prediction': list(prediction)})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Model not loaded'}), 500

if __name__ == '__main__':
    app.run(debug=True)
