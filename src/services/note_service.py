from base.diary import Diary
from base.user import User

from working.create_note import (create_note as default_note_re)

from working.create_user import (create_user as default_user_re)


class InvalidCredentialsError(Exception):
    pass


class UsernameAlreadyExistsError(Exception):
    pass


class NoteService:
    """Luokka, joka hoitaa sovelluslogiikkaa
    """
    def __init__(self, create_note=default_note_re, create_user=default_user_re):
        """Konstruktori, joka luo sovelluslogiikkaa hoitavan avun

        Args:
            create_note (optional): oletuksena Note-olio, jolla Note-luokan metodit
            create_user (optional): oletuksena AboutUsers-olio, jolla AboutUsers-luokan metodit
        """
        
        self._user = None
        self._create_note = create_note
        self._create_user = create_user

    def diary_note(self, note):
        """Kirjaa uuden muistiinpanon

        Args:
            note: merkkijono, jossa säähavainto

        Returns:
            Kirjattu muistiinpano Diary-olio-muodossa
        """

        diary = Diary(note=note, user=self._user)
        return self._create_note.new_note(diary)

    def get_notes(self):
        """Palauttaa käyttäjän kirjaamat muistiinpanot

        Returns:
            Lista käyttäjän muistiinpanoja
        """

        notes = self._create_note.show_by_name(self._user)

        return notes

    def login(self, username):
        """Sisäänkirjautuminen käyttäjänimellä

        Args:
            username: merkkijono, joka on yksilöllinen käyttäjänimi

        Raises:
            InvalidCredentialsError: virhe, joka nousee, jos käyttäjänimeä ei löydy rekisteristä

        Returns:
            Kirjautunut käyttäjä User-oliona
        """

        user = self._create_user.find_by_name(username)
        if not user:
            raise InvalidCredentialsError("Virheellinen käyttäjänimi")
        
        self._user = user
        return user

    def see_current_user(self):
        """Palauttaa sisäänkirjautuneen käyttäjänimen

        Returns:
            Kirjautununeen käyttäjänimi User-oliona
        """
        return self._user

    #def see_users(self):
        #"""Palauttaa kaikki käyttäjänimet

        #Returns:
            #Lista käyttäjänimiä
        #"""
        #return self._create_user.show_users()

    def logout(self):
        """Uloskirjaa sisälläolevan käyttäjän
        """
        self._user = None

    def create_new_user(self, username, login=True):
        """Luo uuden käyttäjän ja kirjaa sen sisään

        Args:
            username: merkkijono, käyttäjätunnus
            login (optional): oletusarvona True. Totuusarvo, joka näyttää, kirjattiinko käyttäjä sisään

        Raises:
            UsernameAlreadyExistsError: virhe, joka kertoo, että käyttäjänimi on jo olemassa

        Returns:
            Uusi käyttäjä User-oliona
        """
        user_exists = self._create_user.find_by_name(username)

        if user_exists:
            raise UsernameAlreadyExistsError("Käyttäjänimi on jo olemassa")

        user = self._create_user.create(User(username))
        #help= (0, user.name)

        if login:
            self._user = user #help

        return user


note_service = NoteService()
