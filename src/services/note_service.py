from base.diary import Diary
from base.user import User

from working.create_note import (create_note as default_note_re)

from working.create_user import (create_user as default_user_re)


class InvalidCredentialsError(Exception):
    pass


class UsernameAlreadyExistsError(Exception):
    pass


class NoteService:
    def __init__(self, create_note=default_note_re, create_user=default_user_re):
        self._user = None
        self._create_note = create_note
        self._create_user = create_user

    def diary_note(self, note):
        # uusi kirjaus
        diary = Diary(note=note, user=self._user)
        return self._create_note.new_note(diary)

    def get_notes(self):
        # näyttää notet
        if not self._user:
            return []

        notes = self._create_note.show_all() #find_by_username(self._user.name)

        return list(notes)

    def login(self, username):
        #print("login")
        user = self._create_user.find_by_name(username)
        if not user:
            raise InvalidCredentialsError("Virheellinen käyttäjänimi")
        self._user = user
        return user

    def see_current_user(self):
        return self._user

    def see_users(self):
        return self._create_user.show_users()

    def logout(self):
        self._user = None

    def create_new_user(self, username, login=True):
        user_exists = self._create_user.find_by_name(username)

        if user_exists:
            raise UsernameAlreadyExistsError("Käyttäjänimi on jo olemassa")

        user = self._create_user.create(User(username))

        if login:
            self._user = user

        return user


note_service = NoteService()
