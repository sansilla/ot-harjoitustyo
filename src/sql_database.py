import os
import sqlite3

db = sqlite3.connect("courses.db")
db.isolation_level = None

def create_tables():
    db.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, note TEXT, date DATETIME)")
