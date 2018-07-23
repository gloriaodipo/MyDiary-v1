import unittest
import json
from . import create_app
from app.models import User, Entry, db

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
                    "password":"mypassword"
                    }
        self.entry_data = {
                    "title": "Freaky friday",
                    "description": "Fun fun fun fun fun fun"
                    }

        self.user1 = User(
            username='testuser',
            email='testuser@email.com',
            password='password')
        self.entry1 = Entry(
            title='I saved a dog',
            description='The dog was cute',
            user_id=1)
        self.test_user = User(
            username='gloria',
            email='glo@mail.com',
            password='password')

    def logged_in_user(self):
        #first create user
        self.client.post(SIGNUP_URL,
        data = json.dumps(self.user_data), content_type = 'application/json')

        #then log in user
        res = self.client.post(LOGIN_URL,
        data=json.dumps({'username': 'gloria', 'password': 'mypassword'}),
        content_type='application/json')
        
        return res

    def tearDown(self):
        '''Clears the database'''
        db.drop()