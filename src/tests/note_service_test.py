import unittest
from base.diary import Diary
from base.user import User
from services.note_service import NoteService, InvalidCredentialsError, UsernameAlreadyExistsError


class TemporaryNote:
    def __init__(self, notes=None):
        self.notes = notes or []

    def show_all(self):
        return self.notes

    def show_by_name(self, username):
        notes = self.show_all()

        these_notes = []
        for note in notes:
            these_notes.append(note)
        return these_notes

    def new_note(self, note):
        self.notes.append(note)

        return note

    def delete(self):
        self.notes = []


class TemporaryAboutUsers:
    def __init__(self, users=None):
        self.users = users or []

    def show_users(self):
        return self.users

    def find_by_name(self, username):
        name = filter(lambda user: user.name == username, self.users)

        name_list = list(name)

        return name_list[0] if len(name_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete(self):
        self.users = []


class TestNoteService(unittest.TestCase):
    def setUp(self):
        self.note_service = NoteService(TemporaryNote(), TemporaryAboutUsers())

        self.note1 = Diary("testataan yhtä")
        self.note2 = Diary("testataan toista")
        self.user_kekkonen = User("kekkonen")

    def login_user(self, user):
        self.note_service.create_new_user(user.name)

    def test_diary_note(self):
        self.login_user(self.user_kekkonen)

        self.note_service.diary_note("testaus")
        notes = self.note_service.get_notes()

        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].note, "testaus")
        self.assertEqual(notes[0].user.name, self.user_kekkonen.name)

    def test_get_notes(self):
        self.login_user(self.user_kekkonen)

        self.note_service.diary_note(self.note1.note)
        self.note_service.diary_note(self.note2.note)

        notes = self.note_service.get_notes()

        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].note, self.note1.note)

    def test_login_with_right_name(self):
        self.note_service.create_new_user(self.user_kekkonen.name)

        user = self.note_service.login(self.user_kekkonen.name)

        self.assertEqual(user.name, self.user_kekkonen.name)

    def test_login_with_invalid_name(self):
        self.assertRaises(InvalidCredentialsError,
                          lambda: self.note_service.login("test_invalid"))

    def test_see_current_user(self):
        self.login_user(self.user_kekkonen)

        curr_user = self.note_service.see_current_user()

        self.assertEqual(curr_user.name, self.user_kekkonen.name)
