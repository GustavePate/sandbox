'''
Created on 11 oct. 2012

@author: guillaume
'''
from monitorperf.data.Ensemble import Ensemble

class LogParser(object):
    
    filetext=[]
    ensemble= Ensemble()
    
    
    def __init__(self,filename):
        self.filetext=[]
        self.ensemble= Ensemble()
        self.loadfile(filename)
        self.toMesure()
    
    def getEnsemble(self):
        return self.ensemble
    
    def loadfile(self,filename):
        print "LogParser.loadfile"
        #Ouvrir le fichier
        f = open(filename, 'r')
        self.filetext=f.readlines()
        f.close()
        
    def toMesure(self):
        for line in self.filetext:
            self.ensemble.addMesure(line)