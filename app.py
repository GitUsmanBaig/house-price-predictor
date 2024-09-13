from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
model_path = 'model.pkl'

# Load the model at startup
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("Model loaded successfully")
else:
    model = None
    print("Failed to load model")

@app.route('/')
def index():
    # Serve the HTML page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            data = request.get_json()
            features = np.array(data['features']).reshape(1, -1)  # Ensure the input features match the expected shape
            prediction = model.predict(features)
            return jsonify({'prediction': list(prediction)})
        except KeyError as ke:
            return jsonify({'error': f'Missing key in data: {str(ke)}'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Model not loaded'}), 500

if __name__ == '__main__':
    app.run(debug=True)
