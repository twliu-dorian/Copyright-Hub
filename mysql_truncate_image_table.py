import mysql.connector
from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute('TRUNCATE TABLE image')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    connect()
