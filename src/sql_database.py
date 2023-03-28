import os
import sqlite3

db.isolation_level = None

def create_tables():
    db.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, note TEXT, date DATETIME)")

def show_users():
    users = db.execute("SELECT name FROM Users_table ORDER BY name").fetchall()
    for user in users:
        print(user)

def create_user(name):
    name = input("Käyttäjänimi: ")
    db.execute("INSERT INTO Users_table (name) VALUES (?)", [name])
    print("Uusi käyttäjä luotu!")

def show_all(name):
    notes = db.execute(f"SELECT note FROM Notes_table, Users_table WHERE Notes_table.user_id = Users_table.id AND Users_table.name = '{name}'").fetchall()
    for note in notes:
        print(note)

def new_note(note):
    note = input("Päivän havainnot: ")
    db.execute("")