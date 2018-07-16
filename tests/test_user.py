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
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully registered")

    def test_wrong_signup(self):
        """Test API cannot successfully register a new user if any field is left blank(POST request)"""
        response = self.client.post(SIGNUP_URL,
            data = json.dumps({'username': 'gloria', 'email':'godipo@gmail.com', 'password':''}) ,
            content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "All fields are required.")
        
    def test_cannot_signup_twice(self):
        """Test API cannot register a user twice(POST request)"""
        self.client.post(SIGNUP_URL,
            data = json.dumps(self.user_data), content_type = 'application/json')
        response2 = self.client.post(SIGNUP_URL, 
            data = json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(response2.status_code, 203)
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "User already exists")
        
    def test_login(self):
        """Test API can successfully log in registered users using username and password (POST request)"""
        self.test_user.save()
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'gloria', 'password': 'password'}),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "You are successfully logged in")
        
    def test_wrong_password(self):
        """Test API cannot authenticate login when wrong password is used (POST request)"""
        self.test_user.save()
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'gloria', 'password': 'wrong_password'}),
            content_type='application/json')
        self.assertEqual(response.status_code, 401)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Username or password is wrong.')
        
    def test_login_nonexistent_user(self):
        """Test API cannot authenticate login when user is nonexistent (POST request)"""
        response = self.client.post(LOGIN_URL,
            data=json.dumps({'username': 'nonexistent', 'password': 'wrong_password'}),
            content_type='application/json')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'User unavailable')