'''
Created on 3 mars 2013

@author: guillaume
'''
from pymongo.mongo_client import MongoClient


if __name__ == '__main__':
    print "ok"
    connection = MongoClient('localhost', 27017)
    db = connection.yeahdb
    print db
    pass