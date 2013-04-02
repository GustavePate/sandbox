#encoding: utf-8
'''
Created on 11 oct. 2012

@author: guillaume
'''

from yaml import load, Loader

class Configuration(object):

    
    logger=''
    initialized=False
    settings={}
    

    def __init__(self,confpath=None):
        '''
        Constructor
        '''
        if confpath != None:
            try:
                print "Configuration Loaded from:",confpath
                f=open(confpath,'r')  
                Configuration.settings=load(f, Loader=Loader)
                Configuration.initialized=True
            finally:
                if f!=None:
                    f.close()
        self.initialized=True
        self.settings = Configuration.settings
            
                
                
    def get(self):
        return self.settings
        
    @staticmethod
    def getInit():
        return Configuration.initialized
    
    @staticmethod
    def getLogger():
        return Configuration.logger
