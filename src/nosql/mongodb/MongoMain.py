'''
Created on 3 mars 2013

@author: guillaume
'''
from pymongo.mongo_client import MongoClient
import itertools
import datetime

NUM_INSERT=100000
MODULO=1000

def modulos(stream):
    for n in stream:
        if n % MODULO == 0:
            yield n


if __name__ == '__main__':

    print "******Connect******"
    start=datetime.datetime.utcnow()
    
    connection = MongoClient('localhost', 27017)
    db = connection.yeahdb
    
    end=datetime.datetime.utcnow()
    result=end-start    
    print db
    print "connection time: ", result

    print ""
    print "******Create Table******"
    start=datetime.datetime.utcnow()
    
    data = {"num": -1,"date": datetime.datetime.utcnow()}
    objectid = db.testtable.insert(data)
    
    end=datetime.datetime.utcnow()
    result=end-start    
    print "create table time: ", result
    print ""    
    print "******Write******"
    keys=[]
    start=datetime.datetime.utcnow()
    for num in itertools.count():
        keys.append(num)
        data = {"num": num,"date": datetime.datetime.utcnow()}
        objectid = db.testtable.insert(data)
        
        if num>=NUM_INSERT:
            break
    end=datetime.datetime.utcnow()
    result=end-start
    print "write time: ", result
    print "write time per record: ", result/NUM_INSERT
    
    print ""
    print "******Read******"
    
    keycoll = modulos(keys)

    start=datetime.datetime.utcnow()
    
    nbread=0
    for i in keycoll :
        nbread+=1
        res=db.testtable.find_one({"num": i})
    
    end=datetime.datetime.utcnow()
    result=end-start
    print "read time: ", result
    print "read time per record: ", result/nbread
    
    print ""
    print "******Delete******"
    
    start=datetime.datetime.utcnow()
    
    db.testtable.remove()
    
    end=datetime.datetime.utcnow()
    result=end-start
    print "delete time: ", result
    print "delete time per record: ", result/NUM_INSERT
    
    print "" 
    print "******Drop******"
    
    start=datetime.datetime.utcnow()
    
    db.testtable.drop()
    
    end=datetime.datetime.utcnow()
    result=end-start
    print "drop time: ", result
    pass