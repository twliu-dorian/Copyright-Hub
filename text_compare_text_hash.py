from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from simhash import Simhash
from ast import literal_eval
import os


compare_file_path  = 'uploads'
# hash_file_path     = '/home/user/Desktop/moc/dataset/text/chinese_writings/hash-value-data'    #change to your own file path

def simhash_similarity(simhash1, simhash2):

    # hash1 = Simhash(text1)
    # hash2 = Simhash(text2)
    #
    # print(bin(hash1.value))
    # print(bin(hash2.value))

    #distance = simhash1.distance(simhash2)
    #print(distance)
    # assert len(simhash1) == len(simhash2)
    hamming_distance = sum(c1 != c2 for c1, c2 in zip(simhash1, simhash2))
    max_hashbit = max(len(simhash1),len(simhash2))

    similar = 1- hamming_distance/max_hashbit
    #print(similar)
    # a  = float(literal_eval(simhash1))
    # b  = float(literal_eval(simhash2))
    #
    #
    #
    # if a>b :
    #     similar = b/a
    # else:
    #     similar = a/b
    #print('similar : ',similar)
    return similar


# if __name__ == '__main__':
def text_compare_hash(filename):
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()

    cursor.execute('SELECT ori_filename, sim_hash FROM text')
    text_hash_data = cursor.fetchall()

    results = ""
    # for filename in os.listdir(compare_file_path):
    if filename.endswith('.txt'):
        
        text_file = open(compare_file_path+'/'+filename)
        text = text_file.read()
        simhash1 = bin(Simhash(text).value)
        #print(type(simhash1))
        #print(simhash1)
        

        for row in text_hash_data:
            # hash_file = open(hash_file_path+'/'+hashfile)
            
            hash_file = row[0]
            simhash2 = row[1]
            if filename == hash_file:
                similarity = simhash_similarity(simhash1, simhash2)
                if(similarity > 0.85):
                    print(filename, "  plagiarizes  ", hash_file ," similarity : ", similarity)
                    results = results + "檔案名稱： "+ str(hash_file) +"\n相似程度：" + str(similarity*100) + "/100\n"
    cursor.close()
    conn.close()
    return results
