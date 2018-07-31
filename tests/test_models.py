from app.models import User, Entry, db
from .base import BaseClass

class TestModels(BaseClass):
    '''Class for models test cases'''
        
    def test_can_save_user(self):
        '''Test successful save operation for user'''
        user = self.user1.save()
        self.assertEqual(1, len(db.users))
        self.assertTrue(isinstance(user, dict))
    
    def test_can_delete_user(self):
        '''Test suucessful deletion of user'''
        self.user1.save()
        self.assertEqual(1, len(db.users))
        user = User.get(id=1)
        user.delete()
        self.assertEqual(0, len(db.users))
    
    def test_can_update_user_details(self):
        '''Test successful update of user deatails'''
        data = {
            'username': 'newusername',
            'email': 'newusername@email.com'}
        self.user1.save()
        user = User.get(id=1)
        user = user.update(data=data)
        self.assertEqual(data['username'], user['username'])
        self.assertEqual(data['email'], user['email'])
    
    def test_get_non_existent_user(self):
        '''Test cannot get non existent user'''
        user = User.get(id=3)
        self.assertEqual('User does not exist.', user['message'])
    
    def test_get_user(self):
        '''Test can get user'''
        self.user1.save()
        user = User.get(id=1)
        self.assertIsInstance(user, User)
        keys = sorted(list(user.view().keys()))
        self.assertListEqual(keys, sorted(['username', 'email', 'id']))
    
    def test_can_save_entry(self):
        '''Test successful save operation after entry addition'''
        self.user1.save()
        entry = self.entry1.save()
        self.assertEqual(1, len(db.entries[1]))
        self.assertIsInstance(entry, dict)
    
    def test_can_update_entry(self):
        '''Test successful update of entries'''
        self.user1.save()
        self.entry1.save()
        entry = Entry.get(id=1, user_id=1)
        data = {
            'title': 'New Title',
            'description': 'New descriptiom'}
        entry = entry.update(data=data)
        self.assertDictContainsSubset(data, entry)
    
    def test_can_get_one_entry(self):
        '''Test can get a single entry'''
        self.user1.save()
        self.entry1.save()
        entry = Entry.get(id=1, user_id=1)
        self.assertIsInstance(entry, Entry)
        keys = sorted(list(entry.view().keys()))
        self.assertListEqual(
            keys, sorted(['title', 'description', 'user_id', 'last_modified', 'created_at', 'id']))
    
    def test_can_get_all_entries(self):
        '''Test can get all diary entries'''
        self.user1.save()
        self.entry1.save()
        entry = Entry.get(user_id=1)
        self.assertIsInstance(entry, dict)
        self.assertEqual(1, len(entry))

    def test_can_delete_an_entry(self):
        '''Test can delete an entry'''
        self.user1.save()
        self.entry1.save()
        entry = Entry.get(user_id=1, id=1)
        self.assertEqual(1, len(db.entries[1]))
        entry.delete()
        self.assertEqual(0, len(db.entries[1]))

    def test_cannot_get_non_existent_entry(self):
        '''Test cannot get an unavailable entry'''
        self.user1.save()
        entry = Entry.get(id=2, user_id=1)
        self.assertEqual('User does not have any entries', entry['message'])
    