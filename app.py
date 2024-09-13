from flask import Flask, request, render_template, jsonify
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if model:
            try:
                features = [
                    float(request.form['medianIncome']),
                    float(request.form['houseAge']),
                    float(request.form['roomsPerHousehold']),
                    float(request.form['bedroomsPerHousehold']),
                    float(request.form['population']),
                    float(request.form['households']),
                    float(request.form['latitude']),
                    float(request.form['longitude'])
                ]
                features = np.array(features).reshape(1, -1)  # Reshape for prediction
                prediction = model.predict(features)
                prediction = prediction[0]  # Take the first (and only) prediction
                result = f"Predicted Price: ${prediction:.2f}"
            except Exception as e:
                result = f"Error: {str(e)}"
        else:
            result = "Error: Model not loaded"
    else:
        result = None
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
