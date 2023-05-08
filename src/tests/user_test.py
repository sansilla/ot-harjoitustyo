import unittest
from base.user import User

class TestBaseUser(unittest.TestCase):
    def setUp(self):
        self.user = User("kekkonen")

    def test_user(self):
        self.assertEqual(self.user.name, "kekkonen")