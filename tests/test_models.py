from app.models import User, Entry, db
from .base import BaseClass

class TestModels(BaseClass):
        
    def test_can_save_user(self):
        user = self.user1.save()
        self.assertEqual(1, len(db.users))
        self.assertTrue(isinstance(user, dict))
    
    def test_can_delete_user(self):
        self.user1.save()
        self.assertEqual(1, len(db.users))
        user = User.get(id=1)
        user.delete()
        self.assertEqual(0, len(db.users))
    
    def test_can_update_user_details(self):
        data = {
            'username': 'newusername',
            'email': 'newusername@email.com'}
        self.user1.save()
        user = User.get(id=1)
        user = user.update(data=data)
        self.assertEqual(data['username'], user['username'])
        self.assertEqual(data['email'], user['email'])
    
    def test_get_non_existent_user(self):
        user = User.get(id=3)
        print(len(db.users))
        self.assertEqual('User does not exist.', user['message'])
    
    def test_get_user(self):
        self.user1.save()
        user = User.get(id=1)
        self.assertIsInstance(user, User)
        keys = sorted(list(user.view().keys()))
        self.assertListEqual(keys, sorted(['username', 'email', 'id']))
    
