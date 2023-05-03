#import time


class Diary:
    """Luokka, joka kuvaa yhtä muistiinpanoa
    """
    def __init__(self, note, user=None):
        """Konstruktori, joka muodostaa muistiinpanon

        Args:
            note: merkkijono, joka kertoo säähavainnon
            user (optional): oletukseltaan None
        """
        self.note = note
        #self.date = date  # sovellus asettaisi tämän automaattisesti uuteen kirjaukseen
        self.user = user
