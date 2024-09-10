# Filename: test.py

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_predict(self):
        # Sample data for testing
        response = self.app.post('/predict', json={
            'features': [0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98]
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue('prediction' in response.get_json())

    def test_predict_error(self):
        # Sending incorrect data format
        response = self.app.post('/predict', json={'wrong_key': 'wrong_value'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in response.get_json())

if __name__ == '__main__':
    unittest.main()
