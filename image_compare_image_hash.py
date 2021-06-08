from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from PIL import Image
import imagehash
import os



a_plagiarism_thres = 6
d_plagiarism_thres = 6
p_plagiarism_thres = 6
w_plagiarism_thres = 6

# hash_file_path = '/home/user/Desktop/moc/dataset/image/moc-image/hash-value-data'
# compare_file_path = '/home/user/Desktop/moc/dataset/image/moc-image/test-image-data'
compare_file_path = 'uploads'


def hamming_distance(hash1, hash2):
    # return(c1 != c2 for c1,c2 in zip(hash1, hash2))
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(hash1, hash2))))

# if __name__ == '__main__':
def image_compare_hash(filename):
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()
    cursor.execute('SELECT ori_filename, a_hash, d_hash, p_hash, w_hash FROM image')
    image_hash_data = cursor.fetchall()

    results = []
    results.clear()
    # for filename in os.listdir(compare_file_path):
    if filename.endswith('.jpg') or filename.endswith('.bmp') or filename.endswith('.png') or filename.endswith('.jpeg'):
        #print(filename)
        a_hash1 = str(imagehash.average_hash(Image.open(compare_file_path+'/'+filename)))
        d_hash1 = str(imagehash.dhash(Image.open(compare_file_path+'/'+filename)))
        p_hash1 = str(imagehash.phash(Image.open(compare_file_path+'/'+filename)))
        w_hash1 = str(imagehash.whash(Image.open(compare_file_path+'/'+filename)))
        # print(a_hash1)
        # print(d_hash1)
        # print(p_hash1)
        # print(w_hash1)

        for row in image_hash_data:
            #f = open(hash_file_path+'/'+comparefile)
            #a_hash2 = f.readline()
            compare_file = row[0]
            a_hash2 = row[1]
            d_hash2 = row[2]
            p_hash2 = row[3]
            w_hash2 = row[4]
            # print("a_hash similarity : ", hamming_distance(a_hash2, a_hash1))
            # print("d_hash similarity : ", hamming_distance(d_hash2, d_hash1))
            # print("p_hash similarity : ", hamming_distance(p_hash2, p_hash1))
            # print("w_hash similarity : ", hamming_distance(w_hash2, w_hash1))
            if filename == compare_file:
              if (hamming_distance(a_hash2, a_hash1) < a_plagiarism_thres) | (hamming_distance(d_hash2, d_hash1) < d_plagiarism_thres) | (hamming_distance(p_hash2, p_hash1) < p_plagiarism_thres) | (hamming_distance(w_hash2,w_hash1) < w_plagiarism_thres):
                print(filename +" plagiarizes " + compare_file)
                print("a_hash similarity : ", hamming_distance(a_hash2, a_hash1))
                print("d_hash similarity : ", hamming_distance(d_hash2, d_hash1))
                print("p_hash similarity : ", hamming_distance(p_hash2, p_hash1))
                print("w_hash similarity : ", hamming_distance(w_hash2, w_hash1))
                results.append(compare_file)
    cursor.close()
    conn.close()
    return results
