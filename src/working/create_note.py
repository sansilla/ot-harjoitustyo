from pathlib import Path
#from base.diary import Diary
#from working.create_user import create_user
from config import NOTES_FILE_PATH


class Note:
    def __init__(self, file_path):
        self._file_path = file_path

    def new_note(self, note):
        notes = self._read()
        notes.append(note)
        self._add(note)
        return note

    def _add(self, note):
        self._is_file_real()
        with open(self._file_path, "a", encoding="UTF-8") as file:
            file.write(str(note.user)+":") #täällä muutos
            file.write(str(note.note)+"\n")
            print("uusi kirjaus:", note)

    def _is_file_real(self):
        Path(self._file_path).touch()

    def _read(self):
        self._is_file_real()
        list1 = []
        with open(self._file_path, encoding="UTF-8") as file:
            for line in file:
                list1.append(str(line))
        #print(list1)
        return list1


create_note = Note(NOTES_FILE_PATH)
