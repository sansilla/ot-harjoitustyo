from sql_database import ???1

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, date DATETIME, note TEXT)")
    connection.commit()

def initialize_sql_database():
    connection = ???1
    create_tables(connection)

if __name__ == "__main__":
    initialize_sql_database()
