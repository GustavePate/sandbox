'''
Created on 11 oct. 2012

@author: guillaume
'''
from monitorperf.utils.Configuration import Configuration

class Filter(object):

    __globalcutoff=500

    def __init__(self,globalcutoff=None):
        if globalcutoff is None:
            self.__globalcutoff=Configuration.settings['global']['GLOBALCUTOFF']
        else:
            self.__globalcutoff=globalcutoff

    def getGlobalcutoff(self):
        return Configuration.settings['global']['GLOBALCUTOFF']
    
    def getRecifcutoff(self):
        return Configuration.settings['global']['RECIFCUTOFF']
    
    def getRecifTRcutoff(self):
        return Configuration.settings['global']['RECIFTRCUTOFF']    
    
    def getHostcutoff(self):
        return Configuration.settings['global']['HOSTCUTOFF']
    
    def getInternalcutoff(self):
        return Configuration.settings['global']['INTERNALCUTOFF']     
    

    globalcutoff = property(getGlobalcutoff, None, None, None)
            