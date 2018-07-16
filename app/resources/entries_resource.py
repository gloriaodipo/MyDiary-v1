from flask import Flask
from flask_restful import Resource, reqparse

from app.models import Entry

class EntryResource(Resource):
    '''Resource for diary entries'''
    parser = reqparse.RequestParser()
    parser.add_argument('title', required = True, type=str)
    parser.add_argument('description', required = True, type=str)

    def post(self, user_id):
        pass

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass        