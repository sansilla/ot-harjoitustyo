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
        diary = Diary(note=note, user=self._user)
        return self._create_note.new_note(diary)
