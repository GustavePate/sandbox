'''
Created on 26 mars 2013

@author: guillaume
'''

import gc
import urllib2
import os

class Utils(object):
    '''
    classdocs
    '''

    def downloadexample(self,filename):
        """ Get a python logo image for this example """
        if not os.path.exists(filename):
            response = urllib2.urlopen(
                'http://www.python.org/community/logos/python-logo.png')
            f = open(filename, 'w')
            f.write(response.read())
            f.close()

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
        