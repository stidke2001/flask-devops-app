# test_aap.py (test file for your Flask app)

import unittest
from aap import app  # Import the Flask app from aap.py

class TestFlaskApp(unittest.TestCase):
    # Set up the test client for Flask app
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test the '/' route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()

