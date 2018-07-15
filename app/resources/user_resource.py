from flask import Flask
from flask_restful import Resource, reqparse

<<<<<<< HEAD
app = Flask(__name__)
api = Api(app)
=======
from app.models import User
from app.database import db
>>>>>>> e670316... Remove app from user resource

class Signup_Resource(Resource):
    '''Resource for user registration'''
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
    parser.add_argument('password', required=True, help='Password cannot be blank')

    def post(self):
        args = Signup_Resource.parser.parse_args()

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
        
