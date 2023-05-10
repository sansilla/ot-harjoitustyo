from sql_database import get_some_service


def drop(service):
    """Poistaa taulukot tietokannasta

    Args:
        service: olio tietokantayhteydelle
    """
    cursor = service.cursor()
    cursor.execute("DROP TABLE IF EXISTS users_table")
    service.commit()


def create_tables(service):
    """Luo taulukot tietokantaan

    Args:
        service: olio tietokantayhteydelle
    """
    cursor = service.cursor()
    cursor.execute(
        "CREATE TABLE users_table (id INTEGER PRIMARY KEY, name TEXT)")
    service.commit()


def initialize_sql_database():
    """Alustaa taulukot
    """
    service = get_some_service()
    drop(service)
    create_tables(service)


if __name__ == "__main__":
    initialize_sql_database()
