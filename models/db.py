# Purpose: MySQL connection for the app. Settings come from .env (see .env.sample).
# Database class (Singleton) added by Maaz Majeed.
import getpass
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # reads .env from the project root

DB_USER = os.environ.get('DB_USER') or getpass.getuser()
DB_NAME = os.environ.get('DB_NAME', 'fall2026_530_emp')


def get_connection():
    """Open a new MySQL connection.

    Uses DB_USER (default: your compsci username) and DB_NAME from .env.
    Returns: mysql.connector connection. Caller must close it.
    """
    connection = mysql.connector.connect(
        user = DB_USER,
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
        # Shared connection must see other users' changes (no stale snapshot between requests)
        self._conn.autocommit = True

    @classmethod
    def get_instance(cls):
        """Return the one shared Database object, creating it on first use.

        Returns: Database
        """
        if cls._instance is None:
            cls._instance = Database()
        return cls._instance

    def query(self, sql, params=None):
        """Run a SELECT.

        sql: SQL string with %s placeholders. params: tuple of values (optional).
        Returns: list of rows as dicts.
        """
        self._conn.ping(reconnect=True)
        cursor = self._conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def execute(self, sql, params=None):
        """Run an INSERT/UPDATE/DELETE and commit.

        sql: SQL string with %s placeholders. params: tuple of values (optional).
        Returns: int, number of rows changed.
        """
        self._conn.ping(reconnect=True)
        cursor = self._conn.cursor()
        cursor.execute(sql, params or ())
        self._conn.commit()
        count = cursor.rowcount
        cursor.close()
        return count
