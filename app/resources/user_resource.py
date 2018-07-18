from flask import Flask
from flask_restful import Resource, reqparse

from app.models import User
from app.decorators import blank

class SignupResource(Resource):
    '''Resource for user registration'''
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True, help='Email cannot be blank', type=str)
    parser.add_argument('password', required=True, help='Password cannot be blank', type=str)

    def post(self):
        args = SignupResource.parser.parse_args()
        password = args.get('password')
        username = args.get('username')
        email = args.get('email')
        if blank(password) or blank(username) or blank(email):
            return {'message': 'All fields are required'}, 400

        username_exists = User.get_user_by_username(username=args['username'])
        email_exists = User.get_user_by_email(email=args['email'])

        if username_exists or email_exists:
            return {'message': 'User already exists'}, 203
        
        user = User(username=args.get('username'), email=args.get('email'), password=password)
        user = user.save()

        return {'message': 'Successfully registered', 'user': user}, 201

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,help='Username cannot be blank', type=str)
    parser.add_argument('password', required=True, help='Password cannot be blank')

    def post(self):
        args = LoginResource.parser.parse_args()
        username = args["username"]
        password = args["password"]
        if blank(username) or blank(password) == '':
            return {'message': 'All fields are required'}, 400

        user = User.get_user_by_username(username)
        if not user:
            return {'message': 'User unavailable'}, 404
        if user.validate_password(password):
            token = user.generate_token()    
            return {"message": "You are successfully logged in", 'user': user.view(), 'token':token}, 200
        return {"message": "Username or password is wrong."}, 401
