from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserSignupAPI(Resource):
    '''Resource for user registration'''
    def post(self):
        pass

class UserLoginAPI(Resource):
    '''Resource for user login'''
    def post(self):
        pass