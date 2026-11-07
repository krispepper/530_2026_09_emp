import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        user = 'bransonjamanram', # your username goes here
        password='',
        host='compsci',
        database='fall_2026_530_emp'
    )
    return connection