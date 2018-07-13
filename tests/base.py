import unittest
import json
from . import create_app
from . import db

class BaseClass(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.user_data = {
                    "username":"gloria", 
                    "email":"gloria@gmail.com",
                    "password":"pass"
                    }
        self.entries = {
                    "entry_id": 5,
                    "title": "Freaky friday",
                    "description": "Fun fun fun fun fun fun"
                    }

    def tearDown(self):
        '''Clears the database'''
        users = []