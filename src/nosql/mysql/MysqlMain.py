# -*- coding: utf-8 -*-
'''
Created on 17 mars 2013

@author: guillaume
'''

import MySQLdb
import itertools
import datetime

NUM_INSERT=100000
MODULO=1000

def modulos(stream):
    for n in stream:
        if n % MODULO == 0:
            yield n

if __name__ == '__main__':
    
    try:
        print "******Connect******"
        start=datetime.datetime.utcnow()
    
        db = MySQLdb.connect(host="localhost", user="test", passwd="test", db="test")
        
        end=datetime.datetime.utcnow()
        print db
        print "connection time: ", end-start 
        
        #create a cursor for the select
        cur = db.cursor()
        cur.execute("SELECT VERSION()")

        data = cur.fetchone()
    
        print "Database version : %s " % data
        

        print ""
        print "******Create Table******"
        start=datetime.datetime.utcnow()
        
        cur.execute("CREATE TABLE IF NOT EXISTS \
            testtable(num INT,text VARCHAR(30),date VARCHAR(30))")

        end=datetime.datetime.utcnow()
        print "create table time: ", end-start
        print ""    
        print "******Write******"
        keys=[]
        start=datetime.datetime.utcnow()
        for num in itertools.count():
            keys.append(num)
            cur.execute("insert into testtable values ("+str(num)+",'bla','"+str(datetime.datetime.utcnow())+"')")
            if num>=NUM_INSERT:
                db.commit()
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
            res=cur.execute("SELECT * from testtable where num="+str(i))
        
        end=datetime.datetime.utcnow()
        result=end-start
        print "read time: ", result
        print "read time per record: ", result/nbread
        
        print ""
        print "******Delete******"
        start=datetime.datetime.utcnow()
        
        cur.execute("delete from testtable")
        db.commit()
        
        end=datetime.datetime.utcnow()
        result=end-start
        print "delete time: ", result
        print "delete time per record: ", result/NUM_INSERT
        
        print "" 
        print "******Drop******"
    
        start=datetime.datetime.utcnow()
    
        cur.execute("drop table testtable")   
        
        end=datetime.datetime.utcnow()
        result=end-start
        print "drop time: ", result     
    
    except db.Error, e:
  
        print "Error %d: %s" % (e.args[0],e.args[1])
    
    finally:    
        
        if db:    
            db.close()
        
    
    pass