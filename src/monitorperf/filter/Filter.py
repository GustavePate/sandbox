'''
Created on 11 oct. 2012

@author: guillaume
'''
from monitorperf.utils.MyConfiguration import Configuration

class Filter(object):

    __globalcutoff=None
    __recifcutoff=None
    __reciftrcutoff=None
    __hostcutoff=None
    __internalcutoff=None

    def __init__(self,globalcutoff=None):
        if globalcutoff is None:
            self.__globalcutoff=Configuration.settings['global']['GLOBALCUTOFF']
        else:
            self.__globalcutoff=globalcutoff

    def setGlobalCutoff(self,c):
        self.__globalcutoff=c
        
    def setInternalCutoff(self,c):
        self.__internalcutoff=c
        
    def setRecifCutoff(self,c):
        self.__recifcutoff=c
        
    def setReciftrCutoff(self,c):
        self.__reciftrcutoff=c
        
    def setHostCutoff(self,c):
        self.__hostcutoff=c

    def getGlobalcutoff(self):
        if self.__globalcutoff:
            res=self.__globalcutoff
        else:
            res=Configuration.settings['global']['GLOBALCUTOFF']
        return res
    
    def getRecifcutoff(self):
        if self.__recifcutoff:
            res=self.__recifcutoff
        else:
            res=Configuration.settings['global']['RECIFCUTOFF']
        return res

    
    def getRecifTRcutoff(self):
        if self.__reciftrcutoff:
            res=self.__reciftrcutoff
        else:
            res=Configuration.settings['global']['RECIFTRCUTOFF']
        return res
 
    
    def getHostcutoff(self):
        if self.__hostcutoff:
            res=self.__hostcutoff
        else:
            res=Configuration.settings['global']['HOSTCUTOFF']
        return res
    
    def getInternalcutoff(self):
        if self.__internalcutoff:
            res=self.__internalcutoff
        else:
            res=Configuration.settings['global']['INTERNALCUTOFF']
        return res   
    

    globalcutoff = property(getGlobalcutoff, None, None, None)
            