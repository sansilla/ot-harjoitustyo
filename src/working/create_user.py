
from sql_database import get_some_service


class AboutUsers:
    """Luokka, joka hoitaa käyttäjistä riippuvat tietokannan muokkaamiset
    """

    def __init__(self, service):
        """Konstruktori
        Args:
            service: tietokantayhteyteen liittyvä olio
        """
        self._service = service

    def show_users(self):
        cursor = self._service.cursor()
        users = cursor.execute(
            "SELECT name FROM users_table").fetchall()
        return users

    def find_by_name(self, username):
        """Palauttaa käyttäjänimen avulla käyttäjän

        Args:
            username: käyttäjänimi, johon liittyvä tunnus palautetaan

        Returns:
            Käyttäjä User-oliona (jos ei löydy tietokannasta, niin None)
        """
        cursor = self._service.cursor()
        cursor.execute("SELECT * FROM users_table WHERE name = ?", [username])
        row = cursor.fetchone()
        return row

    def create(self, user):
        """Tallettaa uuden käyttäjän tietokantaan

        Args:
            user: Tallennettava uusi käyttäjä User-oliona

        Returns:
            User-oliomuotoinen käyttäjä
        """
        cursor = self._service.cursor()
        cursor.execute(
            "INSERT INTO users_table (name) VALUES (?)", (user.name, ))
        self._service.commit()
        id = cursor.lastrowid
        return (id, user.name)
        #return user.name

    def delete(self):
        """Poistaa käyttäjät
        """
        cursor = self._service.cursor()
        cursor.execute("DELETE FROM users_table")
        self._service.commit()



# hehehehehe

create_user = AboutUsers(get_some_service())
