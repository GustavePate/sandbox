'''
Created on 11 oct. 2012

@author: guillaume
'''
from monitorperf.Configuration import Configuration

class Filter(object):

    __globalcutoff=Configuration.GLOBALCUTOFF
    __recifcutoff=Configuration.RECIFCUTOFF
    __reciftrcutoff=Configuration.RECIFTRCUTOFF    
    __hostcutoff=Configuration.HOSTCUTOFF  
    __internalcutoff=Configuration.INTERNALCUTOFF

    def __init__(self,globalcutoff=None):
        if globalcutoff is None:
            self.__globalcutoff=Configuration.GLOBALCUTOFF
        else:
            self.__globalcutoff=globalcutoff

    def getGlobalcutoff(self):
        return self.__globalcutoff
    
    def getRecifcutoff(self):
        return self.__recifcutoff
    
    def getRecifTRcutoff(self):
        return self.__reciftrcutoff    
    
    def getHostcutoff(self):
        return self.__hostcutoff
    
    def getInternalcutoff(self):
        return self.__internalcutoff       
    

    globalcutoff = property(getGlobalcutoff, None, None, None)
            