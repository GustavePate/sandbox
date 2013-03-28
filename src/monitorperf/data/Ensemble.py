#encoding: utf-8
'''
Created on 11 oct. 2012

@author: guillaume
'''
from monitorperf.data.Mesure import Mesure

class Ensemble(object):
    '''
    classdocs
    '''

    mesures=[]

    def __init__(self):
        '''
        Constructor
        '''
        self.mesures=[]
        
    def addMesure(self,line):
        me = Mesure(line)
        self.mesures.append(me)
        
    def __str__(self):
        #return '{0:53} {1:10} {2:10} {3:.5f} {4:10} {5:8}'.format(self.getNom(),self.getRealSize(),self.getSize(), self.getRealAge(),self.getAge(),self.getDate())
        res=""
        for m in self.mesures:
            res = res + str(m)
        return '{0:53}'.format(res)   
            
    def listMesures(self):     
        for m in self.mesures:
            #print m.getTime()
            print '{0:25};{1:25};{2:8};{3:8};{4:3};{5:8};{6:3};{7:8}'.format(m.getServiceName(),m.getFunctionalData(),m.getGlobalResponseTime(),m.getRecifResponseTime(),m.getRecifCallNumber(),m.getHostResponseTime(),m.getHostCallNumber(),m.getTime())
            #print '{0:25};{1:25};{2:8};{3:8}'.format(m.getServiceName(),m.getFunctionalData(),m.getGlobalResponseTime(),m.getRecifResponseTime(),m.getRecifCallNumber(),m.getHostResponseTime(),m.getHostCallNumber(),m.getTime())    
