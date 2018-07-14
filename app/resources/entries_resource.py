from flask import Flask
from flask_restful import Api, Resource

from app.models import User
from app.database import db

app = Flask(__name__)
api = Api(app)

class Entry_API(Resource):
    '''Resource for diary entries'''
    def post(self):
        pass

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass        