# Filename: main.py

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def load_data():
    data = fetch_california_housing()
    return data.data, data.target

def preprocess_data(X, y):
    # Implement any additional preprocessing here if needed
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model trained with MSE: {mse}")
    return model

def save_model(model, filename='model.pkl'):
    joblib.dump(model, filename)

def main():
    X, y = load_data()
    X, y = preprocess_data(X, y)
    model = train_model(X, y)
    save_model(model)

if __name__ == '__main__':
    main()
