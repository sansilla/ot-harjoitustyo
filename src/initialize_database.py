from sql_database import get_some_service

def create_tables(service):
    cursor = service.cursor()
    cursor.execute("CREATE TABLE Users_table (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE Notes_table (id INTEGER PRIMATY KEY, user_id INTEGER REFERENCES Users_table, date DATETIME, note TEXT)")
    service.commit()

def initialize_sql_database():
    service = get_some_service()
    create_tables(service)

if __name__ == "__main__":
    initialize_sql_database()
