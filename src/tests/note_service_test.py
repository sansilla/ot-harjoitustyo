import unittest
from base.diary import Diary
from base.user import User
from services.note_service import NoteService, InvalidCredentialsError, UsernameAlreadyExistsError

class TemporaryNote:
    def __init__(self, notes=None):
        self.notes = notes or []

    def show_all(self):
        return self.notes
    
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
    
    def find_by_name(self):
        pass

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

    def test_diary_note(self, note):
        pass
