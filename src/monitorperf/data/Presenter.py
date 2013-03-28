#encoding: utf-8
'''
Created on 24 déc. 2012

@author: guillaume
'''
from monitorperf.filter.Filter import Filter
from monitorperf.Configuration import Configuration
from monitorperf.data.Ensemble import Ensemble
import numpy as numpy

class Presenter(object):
    '''
    classdocs
    '''
    ens=Ensemble()

    def __init__(self,ens):
        '''
        Constructor
        '''
        self.ens=ens
        print "Presenter constructor, ensemble size: ",len(self.ens.mesures)
    
    def getGlobalX(self):
        res=[]
        for m in self.ens.mesures:
            res.append(m.getTime())
        return res
    
    def getGlobalResponseTimes(self,activatefiltr=True):
        y=[]
        filtr=Filter()
        for m in self.ens.mesures:
            if (activatefiltr and (m.getGlobalResponseTime()>filtr.getGlobalcutoff())):
                y.append(filtr.getGlobalcutoff())
            else:
                y.append(m.getGlobalResponseTime())
        return y
    
    def getAvgGlobalResponseTimes(self):
        y=self.getGlobalResponseTimes(False)
        window= numpy.ones(int(Configuration.WINDOWSSIZE))/float(Configuration.WINDOWSSIZE)
        res=numpy.convolve(y, window, 'same')
        return res
    
    def getRecifResponseTimes(self,activatefiltr=True):
        y=[]
        filtr=Filter()
        for m in self.ens.mesures:
            if (activatefiltr and (m.getRecifResponseTime()>filtr.getRecifcutoff())):
                y.append(filtr.getRecifcutoff())
            else:
                y.append(m.getRecifResponseTime())
        return y
    
    def getAvgRecifResponseTimes(self):
        y=self.getRecifResponseTimes(False)
        window= numpy.ones(int(Configuration.WINDOWSSIZE))/float(Configuration.WINDOWSSIZE)
        res=numpy.convolve(y, window, 'same')
        return res
    
    def getRecifTRResponseTimes(self,activatefiltr=True):
        y=[]
        filtr=Filter()
        for m in self.ens.mesures:
            if (activatefiltr and (m.getRecifTRResponseTime()>filtr.getRecifTRcutoff())):
                y.append(filtr.getRecifTRcutoff())
            else:
                y.append(m.getRecifTRResponseTime())
        return y
    
    def getAvgRecifTRResponseTimes(self):
        y=self.getRecifTRResponseTimes(False)
        window= numpy.ones(int(Configuration.WINDOWSSIZE))/float(Configuration.WINDOWSSIZE)
        res=numpy.convolve(y, window, 'same')
        return res    
    
    
    def getHostResponseTimes(self,activatefiltr=True):
        y=[]
        filtr=Filter()
        for m in self.ens.mesures:
            if (activatefiltr and (m.getHostResponseTime()>filtr.getHostcutoff())):
                y.append(filtr.getHostcutoff())
            else:
                y.append(m.getHostResponseTime())
        return y
    
    def getAvgHostResponseTimes(self):
        y=self.getHostResponseTimes(False)
        window= numpy.ones(int(Configuration.WINDOWSSIZE))/float(Configuration.WINDOWSSIZE)
        res=numpy.convolve(y, window, 'same')
        return res    
    
    def getInternalResponseTimes(self,activatefiltr=True):
        y=[]
        filtr=Filter()
        for m in self.ens.mesures:
            if (activatefiltr and (m.getSPCResponseTime()>filtr.getInternalcutoff())):
                y.append(filtr.getInternalcutoff())
            elif(m.getSPCResponseTime()<0):
                y.append(filtr.getInternalcutoff())
            else:
                y.append(m.getSPCResponseTime())
        return y
    
    def getAvgInternalResponseTimes(self):
        y=self.getInternalResponseTimes(False)
        window= numpy.ones(int(Configuration.WINDOWSSIZE))/float(Configuration.WINDOWSSIZE)
        res=numpy.convolve(y, window, 'same')
        return res        
    
    
    def setFilter(self,filtr):
        for m in self.ens.mesures:
            if m.getGlobalResponseTime()>filtr.getGlobalcutoff():
                m.setGlobalResponseTime(filtr.getGlobalcutoff())

