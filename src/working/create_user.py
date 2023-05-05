from base.user import User
from sql_database import get_some_service


class AboutUsers:
    def __init__(self, service):
        self._service = service

    def show_users(self): #tarvitseeko tätä enää?
        cursor = self._service.cursor()
        users = cursor.execute(
            "SELECT name FROM users_table").fetchall()  # ORDER BY name
        return users

    def find_by_name(self, username):
        cursor = self._service.cursor()
        cursor.execute("SELECT * FROM users_table WHERE name = ?", [username])
        row = cursor.fetchone()
        #print(row)
        return row # muutos !!!

    def create(self, user):
        cursor = self._service.cursor()
        cursor.execute("INSERT INTO users_table (name) VALUES (?)", (user.name, ))
        self._service.commit()
        return user

    def delete(self):
        cursor = self._service.cursor()
        cursor.execute("DELETE FROM users_table")
        self._service.commit()


create_user = AboutUsers(get_some_service())
