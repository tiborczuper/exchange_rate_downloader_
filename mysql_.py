import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Borkauszkar24",
            database="exchange_rates"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        return False
    return False
