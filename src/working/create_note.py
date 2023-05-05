from pathlib import Path
from base.diary import Diary
from base.user import User
from working.create_user import create_user
from config import NOTES_FILE_PATH


class Note:
    """Luokka, joka hoitaa muistiinpanoista riippuvat tietokannan muokkaamiset
    """
    def __init__(self, file_path):
        """Konstruktori

        Args:
            file_path: reitti tehtävät tallentavaan tiedostoon
        """
        self._file_path = file_path

    def new_note(self, note):
        """Luo uuden muistiinpanon ja tallentaa sen tietokantaan

        Args:
            note: muistiinpano, joka halutaan tallentaa

        Returns:
            Muistiinpano (pelkkänä tekstinä)
        """
        #print(note.user)
        notes = self._read()
        notes.append(note)
        self._add(note)
        return note
    
    def show_all(self):
        """Palauttaa muistiinpanot

        Returns:
            Palauttaa listan muistiinpanoja
        """
        return self._read()

    def _add(self, note):
        self._is_file_real()
        # alempaan: w vai a ?????
        with open(self._file_path, "a", encoding="UTF-8") as file:
            file.write(str(note.user)+":")
            file.write(str(note.note)+"\n")
            print("uusi kirjaus:", note)

    def _is_file_real(self):
        Path(self._file_path).touch()

    def _read(self):
        self._is_file_real()
        list1 = []
        with open(self._file_path, encoding="UTF-8") as file:
            for line in file:
                line = line.replace("\n", "")
                parts = line.split(":")
                user_item = parts[0]
                note = parts[1]
                #apu = parts[0].split("'")
                #print(apu[1])
                #usse = create_user.find_by_name(apu[1])
                #print(usse)
                #if str(usse) in line:
                list1.append(str(note))
        return list1
    
    def delete(self):
        """Poistaa muistiinpanot
        """
        with open(self._file_path, "w", encoding="UTF-8") as file:
            file.write("")


create_note = Note(NOTES_FILE_PATH)
