#encoding: utf-8
'''
Created on 3 mars 2013

@author: guillaume
'''


import cql
import datetime
import itertools
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

NUM_INSERT=100000
MODULO=1000

def modulos(stream):
    for n in stream:
        if n % MODULO == 0:
            yield n

if __name__ == '__main__':
    

    print "******Connect******"
    start=datetime.datetime.utcnow()
    
    pool=ConnectionPool('CassandraTest',['localhost:9160'])
    col_fam=ColumnFamily(pool,'test')
    
    end=datetime.datetime.utcnow()
    result=end-start    
    print col_fam
    print "connection time: ", result

    print ""
    print "******Create Table******"
    start=datetime.datetime.utcnow()
    

    
    end=datetime.datetime.utcnow()
    result=end-start    
    print "create table time: ", result
    print ""    
    print "******Write******"
    col_fam=ColumnFamily(pool,'users')
    print col_fam
    
    col_fam.insert('John',{'email':'john@gmail.com',"birthdate":"25/09/1979"})
    print "ok"


    
    keys=[]
    start=datetime.datetime.utcnow()
    for num in itertools.count():
        keys.append(num)
        data = {"num": '%d' % num,"date": str(datetime.datetime.utcnow())}
        objectid = col_fam.insert(str(num),data)
        
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
        res = col_fam.get(str(i))
    
    end=datetime.datetime.utcnow()
    result=end-start
    print "read time: ", result
    print "read time per record: ", result/nbread
    
    print ""
    print "******Delete******"
    
    start=datetime.datetime.utcnow()
    
    #col_fam.remove('John')
    col_fam.truncate()
    
    end=datetime.datetime.utcnow()
    result=end-start
    print "delete time: ", result
    print "delete time per record: ", result/NUM_INSERT
    
    print "" 
    print "******Drop******"
    
    start=datetime.datetime.utcnow()
    

    
    end=datetime.datetime.utcnow()
    result=end-start
    print "drop time: ", result
    pass
