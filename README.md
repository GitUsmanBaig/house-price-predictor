
# House Price Predictor

This repository hosts a Flask-based web application designed to predict house prices using a RandomForestRegressor model trained on housing data. It includes a CI/CD pipeline utilizing GitHub Actions for automated testing and deployment across different environments.

## View deployed model
https://house-price-predictor-online-d4845b3ba057.herokuapp.com/

## Features

- **Flask API**: Handles prediction requests through RESTful endpoints.
- **Machine Learning Model**: Utilizes RandomForestRegressor for predicting house prices.
- **CI/CD Pipeline**: Automated workflows for continuous integration and deployment using GitHub Actions.
- **Frontend Interface**: Provides a user-friendly interface for data input and displays predictions.

## Project Structure

```
house-price-predictor/
│
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── tests/
│   └── app_test.py
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── app.py
├── requirements.txt
├── Dockerfile
├── Procfile
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Docker (optional for containerization)
- Heroku CLI (optional for Heroku deployment)

### Installation

Clone the repository:

```
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Run the application locally:

```
python app.py
```

## Usage

Access the web application by navigating to `http://localhost:5000` after starting the server. Enter the required details in the provided form and submit to receive the predicted house price.

## Testing

Execute the automated tests:

```
pytest
```

## Deployment

The project is configured for deployment on Heroku using Docker. Updates to the `main`, `dev`, and `staging` branches trigger corresponding automated deployments through GitHub Actions.

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes or enhancements.

## License

Distributed under the MIT License. See `LICENSE` for more information.


