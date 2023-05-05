import unittest
from working.create_note import create_note
from working.create_user import create_user
from base.diary import Diary
from base.user import User

class TestNote(unittest.TestCase):
    def setUp(self):
        create_user.delete()
        create_note.delete()

        self.note1 = Diary("testaus 1")
        self.note2 = Diary("testaus 2")
        self.user_kekkonen = User("kekkonen")
        self.user_sale = User("sale")

    def test_new_note(self):
        create_note.new_note(self.note1)
        notes = create_note.show_all()

        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0], self.note1.note)

    def test_show_all(self):
        create_note.new_note(self.note1)
        create_note.new_note(self.note2)
        notes = create_note.show_all()

        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0], self.note1.note)
        self.assertEqual(notes[1], self.note2.note)

    def test_delete(self):
        create_note.new_note(self.note1)
        notes = create_note.show_all()

        self.assertEqual(len(notes), 1)

        create_note.delete()

        notes = create_note.show_all()

        self.assertEqual(len(notes), 0)