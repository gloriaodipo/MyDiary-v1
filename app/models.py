class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def check_password(self, password):
        if password == self.password:
            return True
        return False

    def user_dict(self):
        return{
            'username': self.username,
            'email': self.email,
            'password': self.password
            }

class Entry():
    entry_id = 1

    def __init__(self, title, description):
        self.id = Entry.entry_id
        self.title = title
        self.description = description
        Entry.entry_id += 1

    def entry_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description
    }        