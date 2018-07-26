from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import check_password_hash, generate_password_hash

class DB():
    '''Class for mock database'''
    def __init__(self):
        self.users = {}
        self.entries = {}
        self.user_count = 0
        self.entry_count = 0
    
    def drop(self):
        self.__init__()
    
db = DB()

class Base():
    '''Base class to be inherited by User and Entry classes'''   
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_modified', datetime.utcnow().isoformat())    
        return self.view()

class User(Base):
    '''Class to model user'''
    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.id = None
        self.created_at = datetime.utcnow().isoformat()
        self.last_modified = datetime.utcnow().isoformat()

    def save(self):
        '''Method for saving a saving a user's registration details'''
        setattr(self, 'id', db.user_count + 1)
        db.users.update({self.id: self})
        db.user_count += 1
        db.entries.update({self.id: {}})
        return self.view()
    
    def validate_password(self, password):
        '''Method for validating password input'''
        if check_password_hash(self.password, password):
            return True
        return False
    
    def delete(self):
        '''Method for deleting a user'''
        del db.users[self.id]
    
    def generate_token(self):
        '''Method for generating token upon login'''
        payload = {'exp': datetime.utcnow()+timedelta(minutes=60),
                    'iat': datetime.utcnow(),
                    'username': self.username,
                    'id': self.id}
        token = jwt.encode(payload, str(current_app.config.get('SECRET')), algorithm='HS256')
        return token.decode()
    
    @staticmethod
    def decode_token(token):
        '''Method for decoding token generated'''
        payload = jwt.decode(token, str(current_app.config.get('SECRET')), algorithms=['HS256'])
        return payload
    
    def view(self):
        '''Method to jsonify object user'''
        keys = ['username', 'email', 'id']
        return {key: getattr(self, key) for key in keys}

    @classmethod
    def get(cls, id):
        '''Method for getting user by id'''
        user = db.users.get(id)
        if not user:
            return {'message': 'User does not exist.'}
        return user
    
    @classmethod
    def get_user_by_email(cls, email):
        '''Method for getting user by email'''
        for id_ in db.users:
            user = db.users.get(id_)
            if user.email == email:
                return user
        return None
    
    @classmethod
    def get_user_by_username(cls, username):
        '''Method for getting user by username'''
        for id_ in db.users:
            user = db.users.get(id_)
            if user.username == username:
                return user
        return None
   
class Entry(Base):
    '''Class to model entry'''
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.id = None
        self.created_at = datetime.utcnow().isoformat()
        self.last_modified = datetime.utcnow().isoformat()
        self.user_id = user_id

    def save(self):
        '''Method for saving entries after posting'''
        setattr(self, 'id', db.entry_count + 1)
        db.entry_count += 1
        db.entries[self.user_id].update({self.id : self})
        return self.view()
          
    def delete(self):
        '''Method for deleting an entry'''
        del db.entries[self.user_id][self.id]
    
    def view(self):
        '''Method to jsonify entry object'''
        keys = ('id', 'title', 'description', 'user_id', 'last_modified', 'created_at')
        return {key: getattr(self, key) for key in keys}
    
    @classmethod
    def get(cls, user_id, id=None):
        '''Method for getting both single and all entries'''
        user_entries  = db.entries.get(user_id)
        if not user_entries:
            return {'message': 'User does not have any entries'}
        if id:
            entry = user_entries.get(id)
            if entry:
                return entry
            return {'message': 'User does not have that entry'}
        return user_entries
