from flask import Flask
from flask_restful import Api, Resource

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