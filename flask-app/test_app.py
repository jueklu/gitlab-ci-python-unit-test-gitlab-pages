import unittest
from flask import Flask
from app import app  # Import the Flask app from your application

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_main_route(self):
        # Send a GET request to the root URL
        response = self.app.get('/')
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the response data is correct
        self.assertEqual(response.data.decode('utf-8'), "Hi there")

if __name__ == "__main__":
    unittest.main()