#encoding: utf-8
'''
Created on 11 oct. 2012

@author: guillaume
'''

import logging
import argparse


from monitorperf.
from monitorperf.Configuration import Configuration
from monitorperf.reader.LogParser import LogParser
from monitorperf.data.Ensemble import Ensemble
from monitorperf.data.Presenter import Presenter
from monitorperf.graph.matplot.Graph import MPChart
from monitorperf.reportmaker.ReportMaker import ReportMaker



def main(log,pngpath,reportpath):
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
    
    log=Log()
    log.setLogger(logging.getLogger(''))
    log.info('YYYYEEEEAAAHHH')
    pass
    
    
    ##############################################
    #     PROGRAM
    ##############################################


    logging.info('***********************************')
    logging.info('MonitorPerf stats: PROCESSING...' )
    logging.info('***********************************')
    logging.info('')

    #@TODO graph temps moyen =>temps moyen dans le titre
    #@TODO declinaison par service
    #@TODO graph nombre appel à dependance / appel => nombre appel moyen dans le titre
    #@TODO declinaison par service
    
    logging.info('MonitorPerf stats: OPENING LOG FILE' )
    ##############################################
    #     Lecture 
    ##############################################
    ens = Ensemble()
    lg = LogParser(Configuration.LOGPATH+Configuration.LOGNAME,ens)
    lg=None
    
    logging.info('LOG PARSER OK')
    #ens.listMesures()
    logging.info('LISTMESURE OK')
    
    ##############################################
    #     Mise en forme des résultats 
    ##############################################
    
    crtl = Presenter(ens)
    
    #ch = Chart(Configuration.GRAPHPATH+Configuration.GRAPHNAME)
    #ch.setData(ens.toData())
    #ch.draw()
    
    #######################################################
    #     Alimentation du chart et constitution du graphe 
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
    
    generatedgraphs=[]
    print "plot 1: global"
    
#    ch = MPChart(Configuration.GRAPHPATH)
#    ch.addData("x",crtl.getGlobalX())
#    ch.addData("detail_global",crtl.getGlobalResponseTimes())  

    res=ch.drawbasicgraph("Temps de reponse Global",ch.data['detail_global'],ch.data['avg_global'])
    generatedgraphs.append(res)

    

    print "plot 2: recif" 
    res=ch.drawbasicgraph("Temps de reponse Recif (partie statique)",ch.data['detail_recif'],ch.data['avg_recif'])
    generatedgraphs.append(res)  

    
    print "plot 3: recif tr"

    res=ch.drawbasicgraph("Temps de reponse Recif (partie tr)",ch.data['detail_reciftr'],ch.data['avg_reciftr'])
    generatedgraphs.append(res)

    
    print "plot 4: host"

    res=ch.drawbasicgraph("Temps de reponse Host",ch.data['detail_host'],ch.data['avg_host'])
    generatedgraphs.append(res)

           
    print "plot 5: internal"
     
    res=ch.drawbasicgraph("Temps de reponse SPC interne (process+db)",ch.data['detail_internal'],ch.data['avg_internal'])
    generatedgraphs.append(res) 

    print "plot 6: all"
    res=ch.drawall("Composition du temps de reponse")
    generatedgraphs.append(res) 
   
    print "plot 7: all2 temps cumulés + surfaces pleines"
    #TODO: nombre d'appel moyen / dependance
    print "plot 8: nombre d'appel moyen / dependance"
    #TODO: (plot 7 avec filtre sur les temps de reponses > 1s
    print "plot 9: (plot 7 avec filtre sur les temps de reponses > 1s)"   
   
    #TODO: concatener les images plutot qu'un pdf
    #TODO: rendre appelable en ligne de commande
    
    rm = ReportMaker(Configuration.REPORTPATH+Configuration.REPORTNAME)
    for graph in generatedgraphs:
        print graph
        rm.addGraph(graph[1], graph[0], "blabla")
    rm.makeit()
        
   
       
    
    logging.info('')
    logging.info('***********************************')
    logging.info('MonitorPerf stats: JOB DONE !' )
    logging.info('***********************************')
    

if __name__ == '__main__':
    



    ##############################################
    #     ARGUMENTS PARSING
    ##############################################

    parser = argparse.ArgumentParser(description='Generate png and pdf reports based on a monitor-perf.log')
    parser.add_argument('log', help='path to the log to analyse', type=str)
    parser.add_argument('-i','--png', help='path to the directory where images will be generated', type=str)
    parser.add_argument('-r','--pdf', help='path to the directory where pdf report will be generated', type=str)
    parser.add_argument('-v', '--verbose', help='increase output verbosity',action='store_true')
    parser.set_defaults(png="./")
    parser.set_defaults(pdf="./report.pdf")
    args= parser.parse_args()
    print args
    print "Program Launched with args:"+str(args)
    print "Log:"+args.log
    print "FilePathToReport:"+args.pdf
    print "DirPathToImages:"+args.png
    
    
    
    








