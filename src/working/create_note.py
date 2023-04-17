from base.diary import Diary
from sql_database import get_some_service
from config import NOTES_FILE_PATH


class Note:
    def __init__(self, file_path):
        self._file_path = file_path
        
        # def new_note(self):
        # kirjaa uusi merkintä
        # ! ! SIIRRETTY DATABASE -OSIOON ! !

        # def show_all(self):
        # näyttää kaikki merkinnät
        # ! ! SIIRRETTY DATABASE -OSIOON ! !


create_note = Note(NOTES_FILE_PATH)
