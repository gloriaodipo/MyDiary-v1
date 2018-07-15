from datetime import datetime

class DB():
    def __init__(self):
        pass
    
    def drop(self):
        pass
    

db = DB()

class User():
    def __init__(self, username, password, email):
        pass

    def save(self):
        pass
    
    def delete(self):
        pass
    
    def update(self, data):
        # Validate keys before passing to data.
        pass

    def view(self):
        pass
    
    @classmethod
    def get(cls, id):
        pass

class Entry():
    def __init__(self, title, description, user_id):
        pass

    def save(self):
        pass
          
    def delete(self):
        pass
    
    def update(self, data):
        # Validate keys before passing to data.
        pass

    def view(self):
        pass
    
    @classmethod
    def get(cls, user_id, id=None):
        pass
