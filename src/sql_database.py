import os
import sqlite3

db.isolation_level = None

def create_tables():
    db.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, note TEXT, date DATETIME)")

def show_users():
    users = db.execute("SELECT name FROM Users_table").fetchall()
    for user in users:
        print(user)

def create_user():
    name = input("Käyttäjänimi: ")
    db.execute("INSERT INTO Users_table (name) VALUES (?)", [name])
    print("Uusi käyttäjä luotu!")


