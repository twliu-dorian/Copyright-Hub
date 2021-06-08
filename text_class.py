from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from simhash import Simhash
from ast import literal_eval
import os

class Text():
    def __init__(self, id, create_time, ori_filename, simhash):
        self.id = id
        self.create_time = create_time
        self.orifilename = ori_filename
        seld.simhash = simhash
