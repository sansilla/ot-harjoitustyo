from sql_database import ???

def create_tables(???):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, date DATETIME, note TEXT)")
    connection.commit()