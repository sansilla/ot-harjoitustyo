import unittest
from working.create_user import create_user
from base.user import User


class TestAboutUsers(unittest.TestCase):
    def setUp(self):
        create_user.delete()
        self.user_kekkonen = User("kekkonen")
        self.user_sale = User("sale")

    def test_create(self):
        create_user.create(self.user_kekkonen) #name pois perästä
        users = create_user.show_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], self.user_kekkonen.name) #name pois perästä

    def test_show_users(self):
        create_user.create(self.user_kekkonen)
        create_user.create(self.user_sale)
        users = create_user.show_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0][0], self.user_kekkonen.name)
        self.assertEqual(users[1][0], self.user_sale.name)

    def test_find_by_name(self):
        create_user.create(self.user_kekkonen)

        user = create_user.find_by_name(self.user_kekkonen.name)

        self.assertEqual(user[1], self.user_kekkonen.name)

