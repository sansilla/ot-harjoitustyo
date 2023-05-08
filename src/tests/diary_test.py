import unittest
from base.diary import Diary

class TestBaseDiary(unittest.TestCase):
    def setUp(self):
        self.note = Diary("testicase", "kekkonen")

    def test_diary(self):
        self.assertEqual(self.note.note, "testicase")
        self.assertEqual(self.note.user, "kekkonen")