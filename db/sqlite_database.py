import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Cria uma conexão ao banco de dados SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
