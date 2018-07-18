from flask import Flask, request
from flask_restful import Resource, reqparse

from app.models import Entry
from app.decorators import token_required, blank

class EntryResource(Resource):
    '''Resource for diary entries'''
    parser = reqparse.RequestParser()
    parser.add_argument('title', required = True, type=str, help='Title cannot be blank')
    parser.add_argument('description', required = True, type=str, help='Description cannot be blank')

    @token_required
    def post(self, user_id):
        args = EntryResource.parser.parse_args()
        title = args.get('title', '')
        description = args.get('description', '')

        if blank(title) or blank(description):
            return {'message': 'All fields are required'}, 400
        entry =  Entry(title=title, user_id=user_id, description=description)
        entry = entry.save()
        return {'message': 'Entry has been published', 'entry': entry}, 201

    @token_required
    def get(self, user_id, entry_id=None):
        user_entry = Entry.get(user_id=user_id, id=entry_id)
        if isinstance(user_entry, Entry):
            return {'message': 'Entry found', 'entry': user_entry.view()}, 200

        if user_entry.get('message'):
            return user_entry, 404
        return {'message': 'Entries found', 'entries': [user_entry[entry].view() for entry in user_entry]}, 200

    @token_required
    def put(self,user_id, entry_id):
        entry = Entry.get(user_id=user_id, id=entry_id)
        if isinstance(entry, dict):
            return entry, 404
        post_data = request.get_json()
        title = post_data.get('title', None)
        description = post_data.get('description', None)
        data = {}
        if title and blank(title) != '':
            data.update({'title': title})
        if description and blank(description) != '':
            data.update({'description', description})
        
        entry = entry.update(data=data)
        return {'message': 'Entry updated successfully', 'new_entry': entry}, 200

    @token_required
    def delete(self, user_id, entry_id):
        user_entry = Entry.get(user_id=user_id, id=entry_id)
        if isinstance (user_entry, Entry):
            user_entry.delete()
            return {"message": "Entry has been deleted"}, 200
        return {"message": "Entry does not exist"}, 404 
