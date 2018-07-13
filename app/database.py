class db():
    '''A mock database to store users and entries'''

    users = []
    
    @classmethod
    def add_user(cls, user):
        cls.users.append(user)

    @classmethod
    def get_user_by_username(cls, username):
        '''Method to get user by username'''
        for user in cls.users:
            if user.username == username:
                return user
            return None

    @classmethod
    def get_user_by_email(cls, email):
        '''Method to get user by email'''
        for user in cls.users:
            if user.email == email:
                return user
            return None