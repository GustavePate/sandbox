'''
Created on 26 mars 2013

@author: guillaume
'''

import gc

class Utils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def dump_garbage(self):
        """
        show us what's the garbage about
        """
            
        # force collection
        print "GARBAGE:"
        gc.collect()
    
        print "GARBAGE OBJECTS:"
        for x in gc.garbage:
            s = str(x)
            if len(s) > 80: s = s[:80]
            print type(x),"\n  ", s
        