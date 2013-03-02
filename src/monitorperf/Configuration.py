#encoding: utf-8
'''
Created on 11 oct. 2012

@author: guillaume
'''

class Configuration(object):
    '''
    classdocs
    '''
    LOGPATH="../../input/"
    LOGNAME="1hour.log"
    #LOGNAME="monitor-perf.ark.full.log"
    GRAPHPATH="../../output/"
    GRAPHNAME="output.png"
    GRAPHMATPLOT="outputmatplot.png"
    REPORTPATH="../../output/"
    REPORTNAME="report.pdf"
    #Sur l'axe du temps écrire un label toutes les X mesures
    XLABELFREQUENCY=900
    
    #Remplacer les temps de reponse > GLOBALCUTOFF par GLOBALCUTOFF
    # (pas pris en compte pour le calcul des moyennes mouvantes)
    GLOBALCUTOFF=500.0
    
    #Remplacer les temps de reponse Recif carac > RECIFCUTOFF par RECIFCUTOFF
    # (pas pris en compte pour le calcul des moyennes mouvantes)
    RECIFCUTOFF=80.0
    
    RECIFTRCUTOFF=100.0
    
    HOSTCUTOFF=250.0
    
    INTERNALCUTOFF=350.0
    
    
    #nb de valeurs prises en comptre pour le calcul de la moyenne flottante
    WINDOWSSIZE=300
    
    logger=''

    def __init__(self):
        '''
        Constructor
        '''
    @staticmethod
    def getLogger():
        return Configuration.logger
