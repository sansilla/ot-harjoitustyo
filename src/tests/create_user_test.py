import unittest
from working.create_user import create_user
from base.user import User

class TestWorkingUser(unittest.TestCase):
    def detUp(self):
        create_user.delete_all()