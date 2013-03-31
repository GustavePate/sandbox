#encoding: utf-8
'''
Created on 11 oct. 2012

@author: arg
'''
##########################################################################################################################################
#   A LIRE AVANT DE LANCER AVEC ECLIPSE
##########################################################################################################################################
# Passer les arguments suivants au programme
# Pour ne pas risquer de committer 
# n'importe quoi n'importe ou:
# ../../ressources/monitorperf/input/1hour.log  -l ARK_ALL -i ../../ressources/monitorperf/output/ -r ../../ressources/monitorperf/output/report.pdf
##########################################################################################################################################


##########################################################################################################################################
#   POUR LANCER EN LIGNE DE COMMANDE 
##########################################################################################################################################
# export PYTHONPATH=/home/guillaume/git/sandbox/src
##########################################################################################################################################


import argparse
import os
import datetime
import sys

from monitorperf.utils.Configuration import Configuration
from monitorperf.reader.LogParser import LogParser
from monitorperf.data.Presenter import Presenter
from monitorperf.graph.matplot.Graph import MPChart
from monitorperf.reportmaker.ReportMaker import ReportMaker


def main(logfullpath,pngpath,reportpath,label):
    
    start=datetime.datetime.now()
    
    ##############################################
    #     PROGRAM
    ##############################################


    print('***********************************')
    print('MonitorPerf stats: PROCESSING...' )
    print('***********************************')
    print('')


    
    ##############################################
    #     Lecture 
    ##############################################
    
    lp=LogParser(logfullpath)
    ens=lp.getEnsemble()  
      
    print('LOG PARSER OK:',logfullpath )

    
    ##############################################
    #     Mise en forme des résultats 
    ##############################################
    
    crtl = Presenter(ens)
    
    #######################################################
    #     Alimentation du chart 
    #######################################################
    
    ch = MPChart(pngpath)
    ch.addData("x",crtl.getGlobalX())
    ch.addData("detail_global",crtl.getGlobalResponseTimes())    
    ch.addData("avg_global",crtl.getAvgGlobalResponseTimes())
    ch.addData("detail_recif",crtl.getRecifResponseTimes())
    ch.addData("avg_recif",crtl.getAvgRecifResponseTimes())
    ch.addData("detail_reciftr",crtl.getRecifTRResponseTimes())
    ch.addData("avg_reciftr",crtl.getAvgRecifTRResponseTimes())
    ch.addData("detail_host",crtl.getHostResponseTimes())
    ch.addData("avg_host",crtl.getAvgHostResponseTimes())    
    ch.addData("detail_internal",crtl.getInternalResponseTimes())
    ch.addData("avg_internal",crtl.getAvgInternalResponseTimes())        
    #print crtl.getRecifResponseTimes()
    crtl=None
    
    #######################################################
    #     Génération des graphes 
    #######################################################    


    
    generatedgraphs=[]
    timestring=str(datetime.datetime.today().strftime('%Y%m%d_%H%M%S_'))
    
    
    print "plot 1: global",len(ch.data['detail_global']),"data points",len(ch.data['avg_global']),"avg points"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Global",ch.data['detail_global'],ch.data['avg_global'])
    generatedgraphs.append(res)

    print "plot 2: recif" ,len(ch.data['detail_recif']),"data points",len(ch.data['avg_recif']),"avg points"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Recif (partie statique)",ch.data['detail_recif'],ch.data['avg_recif'])
    generatedgraphs.append(res)  

    
    print "plot 3: recif tr",len(ch.data['detail_reciftr']),"data points",len(ch.data['avg_reciftr']),"avg points"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Recif (partie tr)",ch.data['detail_reciftr'],ch.data['avg_reciftr'])
    generatedgraphs.append(res)

    
    print "plot 4: host",len(ch.data['detail_host']),"data points",len(ch.data['avg_host']),"avg points"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Host",ch.data['detail_host'],ch.data['avg_host'])
    generatedgraphs.append(res)

           
    print "plot 5: internal",len(ch.data['detail_internal']),"data points",len(ch.data['avg_internal']),"avg points"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse SPC interne (process+db)",ch.data['detail_internal'],ch.data['avg_internal'])
    generatedgraphs.append(res) 

    print "plot 6: all",len(ch.data['detail_global']),"data points",len(ch.data['avg_global']),"avg points"
    res=ch.drawall(timestring+label+"_Composition du temps de reponse")
    generatedgraphs.append(res) 
   
    print "plot 7: all2 temps cumulés + surfaces pleines"
    
    
    print "plot 8: nombre d'appel moyen / dependance"
    
    
    print "plot 9: (plot 7 avec filtre sur les temps de reponses > 1s)"   

    rm = ReportMaker(reportpath)
    for graph in generatedgraphs:
        print graph
        rm.addGraph(graph[1], graph[0], "commentaires...")
    rm.makeit()
    print "report generated:",reportpath
        
    rm=None
    generatedgraphs=None
    
    end=datetime.datetime.now()    
    delta=end-start
    
    print('')
    print('*********************************************************')
    print('MonitorPerf stats: JOB DONE  in '+str(delta)+' !!!!')
    print('*********************************************************')
    

if __name__ == '__main__':
    
    ###################################
    #recuperer  et initialiser la  conf
    ################################### 
    fullpath=os.path.join(os.getcwd(),sys.argv[0])

    pathelements=[]
    pathelements=fullpath.split("/")
    #supprimer le nom du .py du path
    del pathelements[-1]

    res="/"
    for e in pathelements:
        res=os.path.join(res,e)
    
    confpath=os.path.join(res,'../../ressources/monitorperf/conf/configuration.yaml')
    print confpath
    conf=Configuration(confpath)
    

    ##############################################
    #     ARGUMENTS PARSING
    ##############################################

    parser = argparse.ArgumentParser(description='Generate png and pdf reports based on a monitor-perf.log')
    parser.add_argument('log', help='path to the log to analyse', type=str)
    parser.add_argument('-i','--png', help='path to the directory where images will be generated', type=str)
    parser.add_argument('-r','--pdf', help='path to the directory where pdf report will be generated', type=str)
    parser.add_argument('-l','--label', help='label added to generated png and pdf', type=str)
    parser.add_argument('-v', '--verbose', help='increase output verbosity',action='store_true')
    parser.set_defaults(label="B2B_ALL")
    parser.set_defaults(png="./")
    parser.set_defaults(pdf="./report.pdf")
    args= parser.parse_args()
    print "Program Launched with args:"+str(args)
    print "Log:"+args.log
    print "FilePathToReport:"+args.pdf
    print "DirPathToImages:"+args.png
    
    print
    
    shouldquit=False
    if not os.path.exists(args.log):
        shouldquit=True
        print "Log does not exist:"+args.log
        
    if os.path.exists(args.pdf):
        shouldquit=True
        print "Report already exists:"+args.pdf
        
    if not os.path.exists(args.png):
        shouldquit=True
        print "Png directory does not exist:"+args.png
        
    if not(shouldquit):
        main(args.log,args.png,args.pdf,args.label)
          
