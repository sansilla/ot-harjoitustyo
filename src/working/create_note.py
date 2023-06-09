from pathlib import Path
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

    def show_by_name(self, username):
        """Palauttaa kirjautuneen käyttäjän muistiinpanot

        Args:
            username: käyttäjänimi, jonka perusteella etsitään Note-oliot

        Returns:
            Lista käyttäjän muistiinpanoja
        """
        notes = self.show_all()

        shown_notes = []

        for note in notes:
            if str(username) in note:
                part = note.split(":")
                note_part = part[1]
                shown_notes.append(note_part)

        return shown_notes

    def _add(self, note):
        self._is_file_real()

        with open(self._file_path, "a", encoding="UTF-8") as file:
            file.write(str(note.user)+":")
            file.write(str(note.note)+"\n")

    def _is_file_real(self):
        Path(self._file_path).touch()

    def _read(self):
        self._is_file_real()

        list1 = []
        with open(self._file_path, encoding="UTF-8") as file:
            for line in file:
                line = line.replace("\n", "")

                list1.append(str(line))

        return list1

    def delete(self):
        """Poistaa muistiinpanot
        """
        with open(self._file_path, "w", encoding="UTF-8") as file:
            file.write("")


create_note = Note(NOTES_FILE_PATH)
