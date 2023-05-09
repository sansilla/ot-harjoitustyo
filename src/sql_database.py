import sqlite3
from config import DATABASE_FILE_PATH

service = sqlite3.connect(DATABASE_FILE_PATH)


def get_some_service():
    return service
