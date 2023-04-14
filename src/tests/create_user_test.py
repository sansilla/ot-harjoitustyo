import unittest
from working.create_user import create_user
from base.user import User
from initialize_database import initialize_sql_database

class TestAboutUsers(unittest.TestCase):
    def setUp(self):
        create_user.delete()
        self.user_kekkonen = User("kekkonen")

    def test_create(self):
        create_user.create(self.user_kekkonen)
        users = create_user.show_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, self.user_kekkonen.name)