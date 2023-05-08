class Diary:
    """Tiettyä muistiinpanoa kuvaava luokka

    Attributes:
        note: muistiinpano, merkkijono
        user: User-olio, muistiinpanon tekijä
    """

    def __init__(self, note, user=None):
        """Konstruktori, joka muodostaa muistiinpanon
        
        Args:
            note: merkkijono, joka kertoo säähavainnon
            user (optional): oletukseltaan None
        """
        self.note = note
        self.user = user
