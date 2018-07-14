from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class UserSignupAPI(Resource):
    '''Resource for user registration'''
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
    parser.add_argument('password', required=True, help='Password cannot be blank')

    def post(self):
        args = UserSignupAPI.parser.parse_args()

        user = User(username=args.get('username'),
            email=args.get('email'), password=args.get('password'))
    
        username_exists = db.get_user_by_username(args['username'])
        email_exists = db.get_user_by_email(args['email'])

        if username_exists:
            return {'message': 'User already exists'}, 203
        elif email_exists:
            return {'message': 'User already exists'}, 203

        db.add_user(user)

        return {'message': 'Successfully registered'}, 201
        
