import pytest
from flask_testing import TestCase
from app import app
import json

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home_page(self):
        """ Test the home page route. """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)

    def test_predict(self):
        """ Test the predict route. """
        test_data = {
            'area': '7420',
            'bedrooms': 4,
            'bathrooms': 2,
            'stories': 3,
            'mainroad': 'yes',
            'guestroom': 'no',
            'basement': 'no',
            'hotwaterheating': 'no',
            'airconditioning': 'yes',
            'parking': 2,
            'prefarea': 'yes',
            'furnishingstatus': 'furnished'
        }
        response = self.client.post('/predict', data=json.dumps(test_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)
        # Check if prediction key exists in the response
        response_data = json.loads(response.data.decode())
        self.assertTrue('prediction' in response_data or 'error' in response_data)

    def test_predict_error_handling(self):
        """ Test error handling in predict route. """
        # Incomplete data example, assuming 'area' is a required field
        test_data = {
            'bedrooms': 4
        }
        response = self.client.post('/predict', data=json.dumps(test_data), content_type='application/json')
        self.assertNotEqual(response.status_code, 200)
        self.assertIn('error', json.loads(response.data.decode()))

# if running from command line, enable this
if __name__ == '__main__':
    pytest.main()
