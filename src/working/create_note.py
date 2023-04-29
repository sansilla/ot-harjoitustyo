from pathlib import Path
from base.diary import Diary
from working.create_user import create_user

# from sql_database import get_some_service
from config import NOTES_FILE_PATH


class Note:
    def __init__(self, file_path):
        self._file_path = file_path

    def new_note(self, note):
        print(note)
        notes = self.show_all()
        notes.append(note)
        self._add(notes)
        return note

    def show_all(self):
        return self._read()

    def find_by_username(self, username):
        pass

    def _add(self, note):
        pass

    def _is_file_real(self):
        Path(self._file_path).touch()

    def _read(self):
        pass


create_note = Note(NOTES_FILE_PATH)
