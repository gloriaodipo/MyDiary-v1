from datetime import datetime

class DB():
    def __init__(self):
        self.users = {}
        self.entries = {}
        self.user_count = 0
        self.entry_count = 0
    
    def drop(self):
        self.users = {}
        self.entries = {}
        self.user_count = 0
        self.entry_count = 0
    

db = DB()

class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.id = None
        self.created_at = datetime.utcnow().isoformat()
        self.last_modified = datetime.utcnow().isoformat()

    def save(self):
        # db.user_count
        setattr(self, 'id', db.user_count + 1)
        db.users.update({self.id: self})
        db.user_count += 1
        db.entries.update({self.id: {}})
        return self.view()
    
    def delete(self):
        del db.users[self.id]
    
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_modified', datetime.utcnow().isoformat())    
        return self.view()

    def view(self):
        keys = ['username', 'email', 'id']
        return {key: getattr(self, key) for key in keys}
    
    @classmethod
    def get(cls, id):
        user = db.users.get(id)
        if not user:
            return {'message': 'User does not exist.'}
        return user

    
class Entry():
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.id = None
        self.created_at = datetime.utcnow().isoformat()
        self.last_modified = datetime.utcnow().isoformat()
        self.user_id = user_id

    def save(self):
        setattr(self, 'id', db.entry_count + 1)
        db.entries[self.user_id].update({self.id : self})
        return self.view()
          
    def delete(self):
        del db.entries[self.user_id][self.id]
    
    def update(self, data):
        # Validate keys before passing to data.
        for key in data:
            setattr(self, key, data[key])
        setattr(self, 'last_modified', datetime.utcnow().isoformat())
        return self.view()

    def view(self):
        keys = ('id', 'title', 'description', 'user_id', 'last_modified', 'created_at')
        return {key: getattr(self, key) for key in keys}
    
    @classmethod
    def get(cls, user_id, id=None):
        user_entries  = db.entries.get(user_id)
        if not user_entries:
            return {'message': 'User does not have any entries'}
        if id:
            return user_entries[id]
        return user_entries
