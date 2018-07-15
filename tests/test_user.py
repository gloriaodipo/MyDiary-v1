import json

from .base import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'

class Test_User_Case(BaseClass):
    '''User test cases'''    

    def test_signup(self):
        """Test API can successfully register a new user (POST request)"""
        response = self.client.post(SIGNUP_URL,
            data = json.dumps(self.user_data), content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Successfully registered")
        self.assertEqual(response.status_code, 201)

    def test_wrong_signup(self):
        """Test API cannot successfully register a new user if any field is left blank(POST request)"""
        response = self.client.post(SIGNUP_URL,
            data = json.dumps({'email':'godipo@gmail.com', 'password': ''}) ,
            content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "All fields required")
        self.assertEqual(response.status_code, 400)

    def test_cannot_signup_twice(self):
        """Test API cannot register a user twice(POST request)"""
        self.client.post(SIGNUP_URL,
            data = json.dumps(self.user_data), content_type = 'application/json')
        response2 = self.client.post(SIGNUP_URL, 
            data = json.dumps(self.user_data), content_type = 'application/json')
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "User already exists")
        self.assertEqual(response2.status_code, 203)

    def test_login(self):
        """Test API can successfully log in registered users using username and password (POST request)"""
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'gloriaodipo', 'password': 'guess'}),
            content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You are successfully logged in")
        self.assertEqual(response.status_code, 200)

    def test_wrong_password(self):
        """Test API cannot authenticate login when wrong password is used (POST request)"""
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'gloriaodipo', 'password': 'wrong_password'}),
            content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'Wrong password.')
        self.assertEqual(response.status_code, 401)

    def test_login_nonexistent_user(self):
        """Test API cannot authenticate login when user is nonexistent (POST request)"""
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'nonexistent', 'password': 'wrong_password'}),
            content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'User unavailable')
        self.assertEqual(response.status_code, 404)

    def test_login_without_all_fields(self):
        pass    