from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from mysql_insert_image_hash import insert_image_hash
from PIL import Image
import imagehash
import os
from datetime import datetime


timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# open_file_path = '/home/user/Desktop/moc/dataset/Media files/2圖片'

open_file_path = 'uploads'


# if __name__ == '__main__':
def image_fingerprint(filename):
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()

    hash = []
    hash.clear()

    #for filename in os.listdir(open_file_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):
        #print(filename)
        new_filename = filename[:-4]
        #print(new_filename)
        #f = open(hash_file_path+'/'+new_filename+"hash.txt", "a")
        a_hash = str(imagehash.average_hash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(a_hash)+'\n')
        d_hash = str(imagehash.dhash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(d_hash)+'\n')
        p_hash = str(imagehash.phash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(p_hash)+'\n')
        w_hash = str(imagehash.whash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(w_hash)+'\n')
        #f.close()
        #insert_image_hash(cursor.lastrowid, timestamp, filename, a_hash, d_hash, p_hash, w_hash)
        hash.append(a_hash)
        hash.append(d_hash)
        hash.append(p_hash)
        hash.append(w_hash)
        # print(a_hash)
        # print(d_hash)
        # print(p_hash)
        # print(w_hash)
    cursor.close()
    conn.close()

    return hash


def image_to_db(filename):
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()

    hash = []
    hash.clear()

    #for filename in os.listdir(open_file_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.bmp'):
        #print(filename)
        new_filename = filename[:-4]
        #print(new_filename)
        #f = open(hash_file_path+'/'+new_filename+"hash.txt", "a")
        a_hash = str(imagehash.average_hash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(a_hash)+'\n')
        d_hash = str(imagehash.dhash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(d_hash)+'\n')
        p_hash = str(imagehash.phash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(p_hash)+'\n')
        w_hash = str(imagehash.whash(Image.open(open_file_path+'/'+filename)))
        #f.write(str(w_hash)+'\n')
        #f.close()
        results = insert_image_hash(cursor.lastrowid, timestamp, filename, a_hash, d_hash, p_hash, w_hash)
        hash.append(a_hash)
        hash.append(d_hash)
        hash.append(p_hash)
        hash.append(w_hash)
        # print(a_hash)
        # print(d_hash)
        # print(p_hash)
        # print(w_hash)
    cursor.close()
    conn.close()

    return results
