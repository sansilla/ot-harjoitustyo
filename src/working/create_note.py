from base.diary import Diary
from pathlib import Path
from working.create_user import create_user
#from sql_database import get_some_service
from config import NOTES_FILE_PATH


class Note:
    def __init__(self, file_path):
        self._file_path = file_path

    def new_note(self, note):
        notes = self.show_all()
        notes.append(note)
        self._write(notes)
        return note

    def show_all(self):
        return self._read()

    def _write(self, notes):
        self._

    def _read(self):
        notes = []


create_note = Note(NOTES_FILE_PATH)
