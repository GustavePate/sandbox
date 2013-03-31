#encoding: utf-8
'''
Created on 28 oct. 2012

@author: guillaume
'''
import matplotlib.pyplot as plot
import matplotlib.ticker as mticker
import os
import math

from monitorperf.utils.Configuration import Configuration




class MPChart(object):
    '''
    classdocs
    '''

    outputpath=""
    data={}
    xlabel=[]
    filterstep=1
    
    

    def f(self,x):
        res= ((x % self.filterstep) == 0)
        #print 'x',x,'res',res
        return res 
    


    
    
    def __init__(self,outputpath):
        '''
        Constructor
        '''
        self.outputpath=outputpath   
        self.data={}
        self.xlabel=[]  
        self.filterstep=1  
    
    def setxlabels(self):
        # objetif 30 points / graphe
        
        self.xlabel=[]
        self.filterstep=math.ceil(float(len(self.data['x']))/float(Configuration.settings['global']['XTICKNUMBER']))
        xlabel_selected=filter(self.f,range(1,len(self.data['x'])))
                               
        for i in xlabel_selected:
            self.xlabel.append(self.data['x'][i])
        
                                               
        

                    
            

    def drawbasicgraph(self,title,pointdata,avgdata):
        
        #fig = figure.Figure(figsize=(10 , 5))
        fig = plot.figure(figsize=(10 , 4))
        
        self.setxlabels()
        
        graph1 = fig.add_subplot(111)
    
        graph1.plot(pointdata,'b_',label="mesures")
        graph1.plot(avgdata,'r-',linewidth=0.5,label="moy. mouv. ("+str(Configuration.settings['global']['WINDOWSSIZE'])+" mesures)")


                        
        #Mise en forme tick        
        plot.xticks(range(len(self.xlabel)),self.xlabel,rotation=45,fontsize="small")
        
        print 'xticks data size:',len(self.xlabel),'print one for each:',self.filterstep
        myLocator = mticker.MultipleLocator(self.filterstep)
        graph1.xaxis.set_major_locator(myLocator)
        
        
        #text
        plot.title(title,fontsize="small")
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
        

    def drawall(self,title):
        fig = plot.figure(figsize=(10 , 5))
        graph2 = fig.add_subplot(111,axisbg='w',rasterized=True,axisbelow=False)
        graph2.plot(self.data['avg_global'],'k-',linewidth=0.5,label="moy. mouv. global")
        graph2.plot(self.data['avg_internal'],'r-',linewidth=0.5,label='moy. mouv. interne SPC')
        graph2.plot(self.data['avg_recif'],'b-',linewidth=0.5,label="moy. mouv. recif")
        graph2.plot(self.data['avg_reciftr'],'g-',linewidth=0.5,label="moy. mouv. reciftr") 
        graph2.plot(self.data['avg_host'],'m-',linewidth=0.5,label="moy. mouv. host")        
        
        
        
        
        plot.title(title)
        plot.xlabel('time')
        plot.ylabel('temps de reponse / ms')
        plot.legend(loc='upper left',prop={'size':6})
        

        
        #Mise en forme tick        
        plot.xticks(range(len(self.xlabel)),self.xlabel,rotation=45)
        plot.grid(True,'major','y')
        
        myLocator = mticker.MultipleLocator(self.filterstep)
        graph2.xaxis.set_major_locator(myLocator)        

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


    