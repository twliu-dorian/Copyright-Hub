from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config

def check_if_file_exists(filename):

    query = "SELECT EXISTS(SELECT * FROM text WHERE ori_filename=" + filename + ");"
    print(query)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)
        rowcount = cursor.rowcount
        print("number of affected rows: {}".format(rowcount))
        if rowcount == 0:
            print("It does not exist")
            return False
        else :
            print("It exists")
            return True
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
