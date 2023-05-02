from pathlib import Path
from base.diary import Diary
from working.create_user import create_user
from config import NOTES_FILE_PATH


class Note:
    def __init__(self, file_path):
        self._file_path = file_path

    def new_note(self, note):
        notes = self.show_all()
        notes.append(note)
        self._add(note)
        return note

    def show_all(self):
        return self._read()

    #def find_by_username(self, username):
        #pass

    def _add(self, note):
        with open(self._file_path, "a") as file:
            file.write(str(note)+"\n")
            print(f"uusi kirjaus:", {note})

    def _is_file_real(self):
        Path(self._file_path).touch()

    def _read(self):
        list1 = []
        with open(self._file_path) as file:
            for line in file:
                list1.append(line)
        print(list1)
        return list1


create_note = Note(NOTES_FILE_PATH)
