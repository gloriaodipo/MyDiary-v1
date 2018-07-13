import json

from .base import BaseClass

SIGNUP_URL = '/api/v1/user/signup'
LOGIN_URL = '/api/v1/user/login'
ADD_ENTRY_URL = 'api/v1/entries'


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
            data = json.dumps(self.entries_data), content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Entry made")
        self.assertEqual(response.status_code, 201)
