from base.user import User
from sql_database import get_some_service

class AboutUsers:
    def __init__(self, service):
        self._service = service

    def show_users(self):
        cursor = self._service.cursor()
        users = cursor.execute("SELECT name FROM Users_table ORDER BY name").fetchall()
        return users

    def create_user(self, name):
        cursor = self._service.cursor()
        #name = input("Luo käyttäjänimi: ")
        cursor.execute("INSERT INTO Users_table (name) VALUES (?)", [name])
        #print("Uusi käyttäjä luotu!")
        self._service.commit()
        return name
    
    def delete(self):
        cursor = self._service.cursor()
        cursor.execute("DELETE FROM Users_table")
        self._service.commit()
    
create_user = AboutUsers(get_some_service())