from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from simhash import Simhash
import os
from mysql_insert_text_hash import insert_hash
from datetime import datetime


timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#open_file_path = '/home/user/Desktop/moc/dataset/Media files/2文字'
open_file_path = 'uploads'

def text_fingerprint(filename):

    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()
    for filename in os.listdir(open_file_path):
        if filename.endswith('.txt'):
            print(filename)
            with open(open_file_path+'/'+filename, encoding='utf8', errors='ignore') as text_file:
                text = text_file.read()
                simhash = bin(Simhash(text).value)
                print(simhash)
                #insert_hash(cursor.lastrowid, timestamp, filename, simhash)
            text_file.close()
        cursor.close()
        conn.close()
        return simhash
    
    
def text_store_db(filename):
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()
    for filename in os.listdir(open_file_path):
        if filename.endswith('.txt'):
            print(filename)
            with open(open_file_path+'/'+filename, encoding='utf8', errors='ignore') as text_file:
                text = text_file.read()
                simhash = bin(Simhash(text).value)
                print(simhash)
                results = insert_hash(cursor.lastrowid, timestamp, filename, simhash)
            text_file.close()
        cursor.close()
        conn.close()
        return results

