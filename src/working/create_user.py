from base.user import User
from sql_database import get_some_service


class AboutUsers:
    def __init__(self, service):
        self._service = service

    def show_users(self):
        cursor = self._service.cursor()
        users = cursor.execute(
            "SELECT name FROM users_table").fetchall()  # ORDER BY name
        return users

    def find_by_name(self, username):
        cursor = self._service.cursor()
        cursor.execute("SELECT * FROM users_table WHERE name = ?", [username])
        row = cursor.fetchone()
        return row

    def create(self, name):
        cursor = self._service.cursor()
        cursor.execute("INSERT INTO users_table (name) VALUES (?)", [name])
        self._service.commit()
        return name

    def delete(self):
        cursor = self._service.cursor()
        cursor.execute("DELETE FROM users_table")
        self._service.commit()


create_user = AboutUsers(get_some_service())
