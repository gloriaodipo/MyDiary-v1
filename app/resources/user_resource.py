from flask import Flask
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User


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
        if password.strip() == '' or username.strip() == '' or email.strip() == '':
            return {'message': 'All fields are required.'}, 400
        password_hash = generate_password_hash(password)

        username_exists = User.get_user_by_username(username=args['username'])
        email_exists = User.get_user_by_email(email=args['email'])

        if username_exists or email_exists:
            return {'message': 'User already exists'}, 203
        
        user = User(username=args.get('username'), email=args.get('email'), password=password_hash)
        user = user.save()

        return {'message': 'Successfully registered', 'user': user}, 201
