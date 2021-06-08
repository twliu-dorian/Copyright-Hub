# -*- coding: UTF-8 -*-
import json
import pprint
import os
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

def recog_audio():
    counter = 0;
    output_res = ""
    # create a Dejavu instance
    djv = Dejavu(config)
    
    # Recognize audio from a file
    song_path = 'uploads/'
    song = " "
    for rec_song in os.listdir(song_path):
      song = song_path + rec_song
      results = djv.recognize(FileRecognizer, song)
      print(f"From file we recognized: \n")
      pprint.pprint(results, sort_dicts=True)
      find1 = results['results'][0]['song_name']
      find1_sim = results['results'][0]['fingerprinted_confidence'] * 100
      if results['results'][1]['song_name']:
        find2 = results['results'][1]['song_name']
        find2_sim = results['results'][1]['fingerprinted_confidence'] * 100
        counter = 2
      if results['results'][2]['song_name']:
        find3 = results['results'][2]['song_name']
        find3_sim = results['results'][2]['fingerprinted_confidence'] * 100
        counter = 3
      
      if counter == 0:
        output_res = "曲目名稱： "+ find1 +"\n相似程度：" + str(find1_sim) + "/100"
      if counter == 2:
        output_res = "曲目名稱： "+ find1 +"\n相似程度：" + str(find1_sim) + "/100\n"+"曲目名稱： "+ find2 +"\n相似程度：" + str(find2_sim) + "/100\n"
      if counter == 3:
        output_res = "曲目名稱： "+ find1 +"\n相似程度：" + str(find1_sim) + "/100\n"+"曲目名稱： "+ find2 +"\n相似程度：" + str(find2_sim) + "/100\n"+"曲目名稱： "+ find3 +"\n相似程度：" + str(find3_sim) + "/100\n"
        
      
      
    return output_res
      
 
