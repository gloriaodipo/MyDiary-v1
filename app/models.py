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
        setattr(self, 'id', db.user_count + 1)
        db.users.update({self.id: self})
        db.user_count += 1
        db.entries.update({self.id: {}})
        return self.view()
    
    def validate_password(self, password):
        if check_password_hash(self.password, password):
            return True
        return False
    
    def delete(self):
        del db.users[self.id]
    
    def generate_token(self):
        payload = {'exp': datetime.utcnow()+timedelta(minutes=60),
                    'iat': datetime.utcnow(),
                    'username': self.username,
                    'id': self.id}
        token = jwt.encode(payload, str(current_app.config.get('SECRET')), algorithm='HS256')
        return token.decode()
    
    @staticmethod
    def decode_token(token):
        payload = jwt.decode(token, str(current_app.config.get('SECRET')), algorithms=['HS256'])
        return payload
    
    def view(self):
        keys = ['username', 'email', 'id']
        return {key: getattr(self, key) for key in keys}

    @classmethod
    def get(cls, id):
        user = db.users.get(id)
        if not user:
            return {'message': 'User does not exist.'}
        return user
    
    @classmethod
    def get_user_by_email(cls, email):
        for id_ in db.users:
            user = db.users.get(id_)
            if user.email == email:
                return user
        return None
    
    @classmethod
    def get_user_by_username(cls, username):
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
        setattr(self, 'id', db.entry_count + 1)
        db.entry_count += 1
        db.entries[self.user_id].update({self.id : self})
        return self.view()
          
    def delete(self):
        del db.entries[self.user_id][self.id]
    
    def view(self):
        keys = ('id', 'title', 'description', 'user_id', 'last_modified', 'created_at')
        return {key: getattr(self, key) for key in keys}
    
    @classmethod
    def get(cls, user_id, id=None):
        user_entries  = db.entries.get(user_id)
        if not user_entries:
            return {'message': 'User does not have any entries'}
        if id:
            entry = user_entries.get(id)
            if entry:
                return entry
            return {'message': 'User does not have that entry'}
        return user_entries
