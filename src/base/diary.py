import time


class Diary:
    def __init__(self, note, date, user=None):
        self.note = note
        self.date = date  # sovellus asettaisi tämän automaattisesti uuteen kirjaukseen
        self.user = user
