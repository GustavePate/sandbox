#encoding: utf-8
'''
Created on 28 oct. 2012

@author: guillaume
'''
import matplotlib.pyplot as plot
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import os
import math
import time
from time import strptime
from time import mktime
from datetime import datetime


from monitorperf.utils.MyConfiguration import Configuration

class MPChart(object):
    '''
    classdocs
    '''

    outputpath=""
    data={}
    xlabel=[]
    filterstep=1
    
    


    


    
    
    def __init__(self,outputpath):
        '''
        Constructor
        '''
        self.outputpath=outputpath   
        self.data={}
        self.xlabel=[]  
        self.filterstep=1  


    def f(self,x):
        res= ((x % self.filterstep) == 0)
        #print 'x',x,'res',res
        return res 
    
    def setxlabels(self,xdata):
        # objetif 30 points / graphe
        
        print "***** setxlabels *******"
        
        
        self.xlabel=[]
        # 1 label tous les ... longueur donnees / 30
        label_freq=float(len(xdata))/float(Configuration.settings['global']['XTICKNUMBER'])
        
        #on arrondi au dessus (voir arrondi au dessous ?)
        self.filterstep=math.ceil(label_freq)
  

        
#        xlabel_selected=filter(self.f,range(1,len(xdata)))
#                               
#        for i in xlabel_selected:
#            self.xlabel.append(xdata[i])
            
        self.xlabel = [xdata[i] for i in range(1,len(xdata)) if ((i % self.filterstep) == 0)]
                               
        

    def log4jtime2datetime(self,xdata):
        x=[]
        for tt in xdata:
            receivedTime = datetime.strptime(tt, "%H:%M:%S,%f")
            x.append(receivedTime)
        return x
            

    def drawbasicgraph(self,title,xdata,pointdata,avgdata):
        
        print '-------------------------------------------------------------'
        print 'Draw gaph:',title
        print 'xdata:',len(xdata)
        print 'pointdata:',len(pointdata)
        print 'avgdata:',len(avgdata)
        global_average=sum(pointdata)/float(len(pointdata))
        print 'avg',global_average
        
        
        
        #fig = figure.Figure(figsize=(10 , 5))
        fig = plot.figure(figsize=(10 , 4))
        
        #self.setxlabels(xdata)
        
        graph1 = fig.add_subplot(111)
        
        
        
        
        x=self.log4jtime2datetime(xdata)
         
        graph1.plot(x,pointdata,'b_',label="mesures")
        graph1.plot(x,avgdata,'r-',linewidth=0.5,label="moy. mouv. ("+str(Configuration.settings['global']['WINDOWSSIZE'])+" mesures)")


                        
        #Mise en forme tick
        plot.xticks(rotation=45,fontsize="small")        
        #plot.xticks(range(len(self.xlabel)),self.xlabel,rotation=45,fontsize="small")
        
        #print 'xticks data size:',len(self.xlabel),'print one for each:',self.filterstep
        #myLocator = mticker.MultipleLocator(self.filterstep)
        #graph1.xaxis.set_major_locator(myLocator)
        
        
        #text
        plot.title(title+" Moyenne: "+str(global_average)+" ms",fontsize="small")
        plot.xlabel('time',fontsize="small")
        plot.ylabel('temps de reponse / ms',fontsize="small")
        plot.legend(loc='upper left',prop={'size':6})
        
        #grille
        plot.grid(True,'major','y')

        #Layout Global
        plot.tight_layout(1.2)
        
        print "sauvegarde....."
        filename=[]
        filename.append(title.lower().strip().replace(' ','_'))
        filename.append(".png")
        filename_str=''.join(filename)
        savepath=os.path.join(self.outputpath,filename_str)
        plot.savefig(savepath)        
        #self.generatedfiles.append((title,''.join(filename)))   
    
        plot.clf()
        plot.close()
        fig.clf()

        return (title,savepath)


    def addData(self,name,points):
        self.data[name]=points
        

    def drawall(self,title,graphpacman,graphhost):
        fig = plot.figure(figsize=(10 , 5))
        graph2 = fig.add_subplot(111,axisbg='w',rasterized=True,axisbelow=False)
        graph2.plot(self.log4jtime2datetime(self.data['x_global']),self.data['avg_global'],'k-',linewidth=0.5,label="moy. mouv. global")
        graph2.plot(self.log4jtime2datetime(self.data['x_internal']),self.data['avg_internal'],'r-',linewidth=0.5,label='moy. mouv. interne SPC')
        graph2.plot(self.log4jtime2datetime(self.data['x_recif']),self.data['avg_recif'],'b-',linewidth=0.5,label="moy. mouv. recif")
        graph2.plot(self.log4jtime2datetime(self.data['x_reciftr']),self.data['avg_reciftr'],'g-',linewidth=0.5,label="moy. mouv. reciftr")
        if graphhost: 
            graph2.plot(self.log4jtime2datetime(self.data['x_host']),self.data['avg_host'],'m-',linewidth=0.5,label="moy. mouv. host")        
        if graphpacman: 
            graph2.plot(self.log4jtime2datetime(self.data['x_pacman']),self.data['avg_pacman'],'m-',linewidth=0.5,label="moy. mouv. pacman")        
        
        
        
        plot.title(title)
        plot.xlabel('time')
        plot.ylabel('temps de reponse / ms')
        plot.legend(loc='upper left',prop={'size':6})
        

        
        #Mise en forme tick        
#        plot.xticks(range(len(self.xlabel)),self.xlabel,rotation=45)
        plot.xticks(rotation=45,fontsize="small") 
        plot.grid(True,'major','y')
        
#        myLocator = mticker.MultipleLocator(self.filterstep)
#        graph2.xaxis.set_major_locator(myLocator)        

        #Layout Global
        plot.tight_layout(1.2)
        print "sauvegarde....."
        
        filename=[]
        filename.append(title.lower().strip().replace(' ','_'))
        filename.append(".png")
        filename_str=''.join(filename)
        savepath=os.path.join(self.outputpath,filename_str)
        plot.savefig(savepath)        
        #self.generatedfiles.append((title,''.join(filename)))   
        plot.clf()
        plot.close()
        fig.clf()
        return (title,savepath)        


    