import json
import filetype
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)
if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)
    djv.fingerprint_directory("uploads", [".mp3"])
    djv.fingerprint_directory("uploads", [".wav"])
