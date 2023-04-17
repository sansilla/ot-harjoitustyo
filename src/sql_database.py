import sqlite3
from config import DATABASE_FILE_PATH

service = sqlite3.connect(DATABASE_FILE_PATH)


def get_some_service():
    return service

# import datetime

# db.isolation_level = None

# def show_all(name):
    # notes = db.execute(f"SELECT note FROM Notes_table, Users_table
    # WHERE Notes_table.user_id = Users_table.id AND Users_table.name = '{name}'").fetchall()
    # for note in notes:
    # print(note)

# def new_note(id, date, note):
    # name = input("Käyttäjänimi: ")
    # date = datetime.now()
    # note = input("Päivän havainnot: ")
    # id = db.execute(f"SELECT id FROM Users_table WHERE name = '{name}'")
    # db.execute("INSERT INTO Notes_table (id, date, note) VALUES (?, ?, ?)", [id, date, note])
