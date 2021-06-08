import json
import filetype
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

def audio_to_db():
    results = []
    output_res = ""
    # create a Dejavu instance
    djv = Dejavu(config)

    results = djv.fingerprint_directory("uploads", [".mp3"])
    results1 = ''.join(results)
    results = djv.fingerprint_directory("uploads", [".wav"])
    results2 = ''.join(results)
    if(results1):
        output_res = results1
    elif(results2):
        output_res = results2
        
    return output_res
