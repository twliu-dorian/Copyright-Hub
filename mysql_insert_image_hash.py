from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
import requests
import hashlib
def insert_image_hash(id, create_time, ori_filename, a_hash, d_hash, p_hash, w_hash):
    query = "INSERT INTO image(id, create_time, ori_filename, a_hash, d_hash, p_hash, w_hash) " \
            "VALUES(%s, %s, %s, %s, %s, %s, %s)"
    args = (id, create_time, ori_filename, a_hash, d_hash, p_hash, w_hash)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        sql = "SELECT * FROM image WHERE ori_filename = %s"
        adr = (ori_filename ,)
        cursor.execute(sql, adr)
        duplicate = cursor.fetchall()
        if duplicate != [] :
            results = str(ori_filename)+' 已經存在於資料庫中,無需存證'
        else:
            cursor.execute(query, args)
            results = '完成存證'
            
            ################## 上鏈 ##################
            with open('uploads/'+ori_filename,"rb") as f:
                bytes = f.read() # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest();
                print(readable_hash)
            
            url = 'https://postchain-test.chainsecurity.asia/preserve/'+ str(readable_hash)
            r1=requests.post(url, json={"token": "moctest"})
            print(r1.status_code)
            print(r1.json())
            ################## 取得上鏈時間戳 ##################
            url2 = url + '?token=moctest'
            r2 = requests.get(url2)
            print(r2.status_code)
            print(r2.json())
            
            if r1.status_code == 200 & r2.status_code == 200:
                results = '完成存證，完成上鏈，時間戳：'+str(r2.json())
        
        conn.commit()
        return results
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


   
