#encoding: utf-8
'''
Created on 24 déc. 2012

@author: guillaume
'''
from monitorperf.filter.Filter import Filter
from monitorperf.utils.MyConfiguration import Configuration
from monitorperf.data.Ensemble import Ensemble
import numpy as numpy
import math

class Presenter(object):
    '''
    classdocs
    '''
    ens=None
    filtr=None

    def __init__(self,ens):
        '''
        Constructor
        '''
        self.ens=ens
        self.filtr=Filter()
        print "Presenter constructor, ensemble size: ",len(self.ens.mesures)
        
        
    #Adjust cutoff
   
    def adjustConfCutoff(self,debug=False):
        #initial cutoff
        if debug:
            print "initial cutoff:"
            print "self.filtr.getGlobalcutoff()",self.filtr.getGlobalcutoff()
            print "self.filtr.getInternalcutoff()",self.filtr.getInternalcutoff()
            print "self.filtr.getRecifcutoff()",self.filtr.getRecifcutoff()
            print "self.filtr.getRecifTRcutoff()",self.filtr.getRecifTRcutoff()
            print "self.filtr.getHostcutoff()",self.filtr.getHostcutoff()
            print "self.filtr.getPacmancutoff()",self.filtr.getPacmancutoff()
        
             
        self.filtr.setGlobalCutoff(math.ceil(max(self.getAvgGlobalResponseTimes()['y'])/100.0)*100)
        self.filtr.setRecifCutoff(math.ceil(max(self.getAvgRecifResponseTimes()['y'])/100.0)*100)
        self.filtr.setReciftrCutoff(math.ceil(max(self.getAvgRecifTRResponseTimes()['y'])/100.0)*100)
        self.filtr.setInternalCutoff(math.ceil(max(self.getAvgInternalResponseTimes()['y'])/100.0)*100)
        
        if len(self.getHostResponseTimes()['y'])>1:
            self.filtr.setHostCutoff(math.ceil(max(self.getAvgHostResponseTimes()['y'])/100.0)*100)
        if len(self.getPacmanResponseTimes()['y'])>1:
            self.filtr.setPacmanCutoff(math.ceil(max(self.getAvgPacmanResponseTimes()['y'])/100.0)*100)
        
                #initial cutoff
        if debug:
            print "adjusted cutoff:"
            print "self.filtr.getGlobalcutoff()",self.filtr.getGlobalcutoff()
            print "self.filtr.getInternalcutoff()",self.filtr.getInternalcutoff()
            print "self.filtr.getRecifcutoff()",self.filtr.getRecifcutoff()
            print "self.filtr.getRecifTRcutoff()",self.filtr.getRecifTRcutoff()
            print "self.filtr.getHostcutoff()",self.filtr.getHostcutoff()
            print "self.filtr.getPacmancutoff()",self.filtr.getPacmancutoff()
        
        
    
    def getAvg(self,dataset):
        y=dataset
        window_size=int(Configuration.settings['global']['WINDOWSSIZE'])
        if window_size>len(y):
            window_size=len(y)/5
        
        window= numpy.ones(window_size)/float(window_size)
        res=numpy.convolve(y, window, 'same')
        return res
        
    def getGlobalResponseTimes(self,activatefiltr=True):
        x=[]
        y=[]
        for m in self.ens.mesures:
            x.append(m.getTime())
            res=m.getGlobalResponseTime()
            if (activatefiltr and (res>self.filtr.getGlobalcutoff())):
                y.append(self.filtr.getGlobalcutoff())
            else:
                y.append(res)
        return {'x':x,'y':y}
    
    
    def getAvgGlobalResponseTimes(self):
        res=self.getGlobalResponseTimes(False)
        return  {'x':res['x'],'y':self.getAvg(res['y'])}
    
    def getRecifResponseTimes(self,activatefiltr=True):
        y=[]
        x=[]
        for m in self.ens.mesures:
            res=m.getRecifResponseTime()
            if res:
                x.append(m.getTime())
                if (activatefiltr and (res>self.filtr.getRecifcutoff())):
                    y.append(self.filtr.getRecifcutoff())
                else:
                    y.append(res)
                
        return {'x':x,'y':y}
    
    def getAvgRecifResponseTimes(self):
        res=self.getRecifResponseTimes(False)
        return  {'x':res['x'],'y':self.getAvg(res['y'])}

    
    def getRecifTRResponseTimes(self,activatefiltr=True):
        y=[]
        x=[]
        for m in self.ens.mesures:
            res=m.getRecifTRResponseTime()
            if res:
                x.append(m.getTime())
                if (activatefiltr and (res>self.filtr.getRecifTRcutoff())):
                    y.append(self.filtr.getRecifTRcutoff())
                else:
                    y.append(res)
        return {'x':x,'y':y}
    
    def getAvgRecifTRResponseTimes(self):
        res=self.getRecifTRResponseTimes(False)
        return  {'x':res['x'],'y':self.getAvg(res['y'])}

        
    
    def getHostResponseTimes(self,activatefiltr=True):
        y=[]
        x=[]
        for m in self.ens.mesures:
            res=m.getHostResponseTime()
            if res:
                x.append(m.getTime())
                if (activatefiltr and (res>self.filtr.getHostcutoff())):
                    y.append(self.filtr.getHostcutoff())
                else:
                    y.append(res)
        return {'x':x,'y':y}
    
    def getAvgPacmanResponseTimes(self):
        res=self.getPacmanResponseTimes(False)
        return  {'x':res['x'],'y':self.getAvg(res['y'])}


    def getPacmanResponseTimes(self,activatefiltr=True):
        y=[]
        x=[]
        for m in self.ens.mesures:
            res=m.getPacmanResponseTime()
            if res:
                x.append(m.getTime())
                if (activatefiltr and (res>self.filtr.getPacmancutoff())):
                    y.append(self.filtr.getPacmancutoff())
                else:
                    y.append(res)
        return {'x':x,'y':y}
    
    def getAvgHostResponseTimes(self):
        res=self.getHostResponseTimes(False)
        return  {'x':res['x'],'y':self.getAvg(res['y'])}
    
    def getInternalResponseTimes(self,activatefiltr=True):
        y=[]
        x=[]
        for m in self.ens.mesures:
            x.append(m.getTime())
            res=m.getSPCResponseTime()
            if (activatefiltr and (res>self.filtr.getInternalcutoff())):
                y.append(self.filtr.getInternalcutoff())
            elif(res<0):
                y.append(self.filtr.getInternalcutoff())
                print 'Presenter: should not append !'
            else:
                y.append(res)
        return {'x':x,'y':y}
    
    def getAvgInternalResponseTimes(self):
        res=self.getInternalResponseTimes(False)
        return  {'x':res['x'],'y':self.getAvg(res['y'])}        
    
    
    def setFilter(self,filtr):
        for m in self.ens.mesures:
            if m.getGlobalResponseTime()>filtr.getGlobalcutoff():
                m.setGlobalResponseTime(self.filtr.getGlobalcutoff())

