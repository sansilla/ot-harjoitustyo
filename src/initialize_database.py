from sql_database import get_some_service


def drop(service):
    cursor = service.cursor()
    cursor.execute("DROP TABLE IF EXISTS users_table")
    service.commit()


def create_tables(service):
    cursor = service.cursor()
    cursor.execute(
        "CREATE TABLE users_table (id INTEGER PRIMARY KEY, name TEXT)")
    service.commit()


def initialize_sql_database():
    service = get_some_service()
    drop(service)
    create_tables(service)


if __name__ == "__main__":
    initialize_sql_database()
