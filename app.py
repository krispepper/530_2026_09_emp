import os
import mysql.connector
from dotenv import load_dotenv, dotenv_values

load_dotenv()

USER = os.getenv('root') # your username goes here, which is 'root'
print('The user is ', USER)

def get_connection():
    connection = mysql.connector.connect(
        user = USER,
        password='', #your password goes here
        host='localhost',
        database='fall_2026_530_emp'
    )