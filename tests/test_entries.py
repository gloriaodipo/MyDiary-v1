import json

from .base import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'
ADD_ENTRY_URL = 'api/v1/entries'
GET_SINGLE_URL = 'api/v1/entries/1'
GET_ALL_URL = 'api/v1/entries'
DELETE_URL = 'api/v1/entries/1'
MODIFY_URL = 'api/vi/entries/1'


class Test_Entry_Case(BaseClass):
    '''Class for entry test cases'''

    def logged_in_user(self):
        #first create user
        self.client.post(SIGNUP_URL,
        data = json.dumps(self.user_data), content_type = 'application/json')

        #then log in user
        self.client.post(LOGIN_URL,
        data=json.dumps({'username': 'gloriaodipo', 'password': 'guess'}),
        content_type='application/json')

    def test_add_entry(self):
        '''Test API can add entry made by logged in user'''
        self.logged_in_user()

        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Entry made")
        self.assertEqual(response.status_code, 201)

    def test_get_single_entry(self):
        '''Test API can get a single diary entry'''
        self.logged_in_user()

        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')

        response = self.client.get (GET_SINGLE_URL,
            data = json.dumps(self.entries), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_all(self):
        '''Test API can get all diary entries'''
        self.logged_in_user()

        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')

        response = self.client.get(GET_ALL_URL,
        data = json.dumps(self.entries), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_entry(self):
        '''Test API can delete a diary entry'''
        self.logged_in_user()

        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')

        response = self.client.get(DELETE_URL,
        data = json.dumps(self.entries), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_modify_entry(self):
        '''Test API can modify a diary entry'''
        self.logged_in_user()

        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')

        response = self.client.put(MODIFY_URL,
            data = json.dumps(dict(title="Modified title")),content_type = ("application/json"))
        self.assertEqual(response.status_code, 200)    

    def test_cannot_add_entry_without_login(self):
        '''Test API cannot add entry if user is not logged in'''

        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Please login first")
        self.assertEqual(response.status_code, 401)

    def test_cannot_get_single_entry(self):
        '''Test API cannot get a single diary entry without login'''
        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')

        response = self.client.get (GET_SINGLE_URL,
            data = json.dumps(self.entries), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)

    def test_cannot_get_all(self):
        '''Test API cannot get all diary entries without login'''
        response = self.client.post(ADD_ENTRY_URL,
            data = json.dumps(self.entries), content_type = 'application/json')

        response = self.client.get(GET_ALL_URL,
        data = json.dumps(self.entries), content_type = 'application/json')
        self.assertEqual(response.status_code, 401)  
        



















