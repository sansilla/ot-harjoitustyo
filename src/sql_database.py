#import os
import sqlite3
from config import DATABASE_FILE_PATH

service = sqlite3.connect(DATABASE_FILE_PATH)

def get_some_service():
    return service

#import datetime

#db = sqlite3.connect("weatherdiary.db") #Pitäisikö tietokantayhteys muodostaa täysin omassa moduulissaan?
#db.isolation_level = None

#def create_tables():
    #db.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    #db.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, date DATETIME, note TEXT)")

#def show_users():
    #users = db.execute("SELECT name FROM Users_table ORDER BY name").fetchall()
    #for user in users:
        #print(user)

#def create_user(name):
    #name = input("Luo käyttäjänimi: ")
    #db.execute("INSERT INTO Users_table (name) VALUES (?)", [name])
    #print("Uusi käyttäjä luotu!")

#def show_all(name):
    #notes = db.execute(f"SELECT note FROM Notes_table, Users_table WHERE Notes_table.user_id = Users_table.id AND Users_table.name = '{name}'").fetchall()
    #for note in notes:
        #print(note)

#def new_note(id, date, note):
    #name = input("Käyttäjänimi: ")
    #date = datetime.now()
    #note = input("Päivän havainnot: ")
    #id = db.execute(f"SELECT id FROM Users_table WHERE name = '{name}'")
    #db.execute("INSERT INTO Notes_table (id, date, note) VALUES (?, ?, ?)", [id, date, note])