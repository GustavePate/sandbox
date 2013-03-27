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

import logging
import argparse
import os
import datetime

from monitorperf.Configuration import Configuration
from monitorperf.reader.LogParser import LogParser
from monitorperf.data.Ensemble import Ensemble
from monitorperf.data.Presenter import Presenter
from monitorperf.graph.matplot.Graph import MPChart
from monitorperf.reportmaker.ReportMaker import ReportMaker


def main(log,pngpath,reportpath,label,start):
    
    ##############################################
    #     INIT CONFIGURATION
    ##############################################

    Configuration.LOGPATH=log    
    Configuration.REPORTPATH=reportpath
    Configuration.GRAPHPATH=pngpath
    
    
    ##############################################
    #     INIT LOGGERS
    ##############################################
    
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='monitorParser.log',
                    filemode='w')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    # set a format which is simpler for console use
    formatter = logging.Formatter('%(levelname)-2s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
    Configuration.logger=logging
    
#    log=Log()
#    log.setLogger(logging.getLogger(''))
#    log.info('YYYYEEEEAAAHHH')
#    pass
    
    
    ##############################################
    #     PROGRAM
    ##############################################


    logging.info('***********************************')
    logging.info('MonitorPerf stats: PROCESSING...' )
    logging.info('***********************************')
    logging.info('')


    
    ##############################################
    #     Lecture 
    ##############################################
    ens = Ensemble()
    LogParser(Configuration.LOGPATH,ens)    
    logging.info('LOG PARSER OK')

    
    ##############################################
    #     Mise en forme des résultats 
    ##############################################
    
    crtl = Presenter(ens)
    
    #######################################################
    #     Alimentation du chart 
    #######################################################
    
    ch = MPChart(Configuration.GRAPHPATH)
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

    #@TODO graph temps moyen =>temps moyen dans le titre
    #@TODO declinaison par service
    #@TODO graph nombre appel à dependance / appel => nombre appel moyen dans le titre
    #@TODO declinaison par service
    #TODO: concatener les images plutot qu'un pdf
    #TODO: (plot 7 avec filtre sur les temps de reponses > 1s
    #TODO: nombre d'appel moyen / dependance
    #TODO: caller qui wget et appelle N fois / B2B / Service(+*)
    
    generatedgraphs=[]
    timestring=str(datetime.datetime.today().strftime('%Y%m%d_%H%M%S_'))
    
    
    print "plot 1: global"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Global",ch.data['detail_global'],ch.data['avg_global'])
    generatedgraphs.append(res)

    print "plot 2: recif" 
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Recif (partie statique)",ch.data['detail_recif'],ch.data['avg_recif'])
    generatedgraphs.append(res)  

    
    print "plot 3: recif tr"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Recif (partie tr)",ch.data['detail_reciftr'],ch.data['avg_reciftr'])
    generatedgraphs.append(res)

    
    print "plot 4: host"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse Host",ch.data['detail_host'],ch.data['avg_host'])
    generatedgraphs.append(res)

           
    print "plot 5: internal"
    res=ch.drawbasicgraph(timestring+label+"_Temps de reponse SPC interne (process+db)",ch.data['detail_internal'],ch.data['avg_internal'])
    generatedgraphs.append(res) 

    print "plot 6: all"
    res=ch.drawall(timestring+label+"_Composition du temps de reponse")
    generatedgraphs.append(res) 
   
    print "plot 7: all2 temps cumulés + surfaces pleines"
    
    
    print "plot 8: nombre d'appel moyen / dependance"
    
    
    print "plot 9: (plot 7 avec filtre sur les temps de reponses > 1s)"   

    
    rm = ReportMaker(Configuration.REPORTPATH)
    for graph in generatedgraphs:
        print graph
        rm.addGraph(graph[1], graph[0], "commentaires...")
    rm.makeit()
        
   
    
    end=datetime.datetime.now()    
    delta=end-start
    
    logging.info('')
    logging.info('*********************************************************')
    logging.info('MonitorPerf stats: JOB DONE  in '+str(delta)+' !!!!')
    logging.info('*********************************************************')
    

if __name__ == '__main__':
    

    start=datetime.datetime.now()
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
        main(args.log,args.png,args.pdf,args.label,start)
          
