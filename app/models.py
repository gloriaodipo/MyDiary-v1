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