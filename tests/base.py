import unittest
import json
from . import create_app, db
SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'

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
                    "title": "Freaky friday",
                    "description": "Fun fun fun fun fun fun"
                    }

    def logged_in_user(self):
        #first create user
        self.client.post(SIGNUP_URL,
        data = json.dumps(self.user_data), content_type = 'application/json')

        #then log in user
        self.client.post(LOGIN_URL,
        data=json.dumps({'username': 'gloriaodipo', 'password': 'guess'}),
        content_type='application/json')

    def tearDown(self):
        '''Clears the database'''
        users = []
        entries = []