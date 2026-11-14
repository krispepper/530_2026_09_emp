# Purpose: MySQL connection for the app. DB_NAME env var picks dev or UAT (default UAT).
# Database class (Singleton) added by Maaz Majeed.
import getpass
import os
import mysql.connector

DB_NAME = os.environ.get('DB_NAME', 'fall2026_530_emp')

def get_connection():
    connection = mysql.connector.connect(
        user = getpass.getuser(), # compsci username
        password='',
        host='127.0.0.1',
        port=3306,
        database=DB_NAME
    )
    return connection


# Singleton: one shared connection, used by the models
class Database:
    _instance = None

    def __init__(self):
        self._conn = get_connection()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Database()
        return cls._instance

    def query(self, sql, params=None):
        self._conn.ping(reconnect=True)
        cursor = self._conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def execute(self, sql, params=None):
        self._conn.ping(reconnect=True)
        cursor = self._conn.cursor()
        cursor.execute(sql, params or ())
        self._conn.commit()
        count = cursor.rowcount
        cursor.close()
        return count
