#encoding: utf-8
'''
Created on 28 oct. 2012

@author: guillaume
'''
import matplotlib.pyplot as plot

from monitorperf.Configuration import Configuration


class MPChart(object):
    '''
    classdocs
    '''

    outputpath=""
    data={}
    xlabel=[]
    
    def __init__(self,outputpath):
        '''
        Constructor
        '''
        self.outputpath=outputpath       
    
    def setxlabels(self):
        
        
        if (self.xlabel==[]):
            #self.xlabel=self.data['x']
#            pass
#            # inutile ?
            for i,j in enumerate(self.data['x']):
                if not((i % Configuration.XLABELFREQUENCY) == 0):
                    self.xlabel.append('')
                else:
                    self.xlabel.append(j)
                    
            

    def drawbasicgraph(self,title,pointdata,avgdata):
        
        #fig = figure.Figure(figsize=(10 , 5))
        fig = plot.figure(figsize=(10 , 4))
        
        self.setxlabels()
        
        graph1 = fig.add_subplot(111)
    
        graph1.plot(pointdata,'b_',label="mesures")
        graph1.plot(avgdata,'r-',linewidth=0.5,label="moy. mouv. ("+str(Configuration.WINDOWSSIZE)+" mesures)")
                        
        #Mise en forme tick        
        plot.xticks(range(len(self.xlabel)),self.xlabel,rotation=45,fontsize="small")
        #TODO gérer proprement le nombre de ticks    
#        majorLocator   = MaxNLocator(nbins=20)
#        graph1.xaxis.set_major_locator(majorLocator)
        
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
        filename.append(self.outputpath)
        filename.append(title.lower().strip().replace(' ','_'))
        filename.append(".png")
        plot.savefig(''.join(filename))        
        #self.generatedfiles.append((title,''.join(filename)))   
    
        plot.clf()
        plot.close()
        fig.clf()

        return (title,''.join(filename))


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

        #Layout Global
        plot.tight_layout(1.2)
        print "sauvegarde....."
        filename=[]
        filename.append(self.outputpath)
        filename.append(title.lower().strip().replace(' ','_'))
        filename.append(".png")
        plot.savefig(''.join(filename))        
        #self.generatedfiles.append((title,''.join(filename)))   
        plot.clf()
        plot.close()
        fig.clf()
        return (title,''.join(filename))        


    