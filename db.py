import getpass
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        user = getpass.getuser(), # compsci username
        password='',
        host='127.0.0.1',
        port=3306,
        database='fall2026_530_emp'
    )
    return connection