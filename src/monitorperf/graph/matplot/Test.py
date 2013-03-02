#encoding: utf-8
'''
Created on 25 déc. 2012

@author: guillaume
'''
from matplotlib.ticker import MultipleLocator, FormatStrFormatter,MaxNLocator,AutoLocator
from matplotlib.dates import MinuteLocator
import numpy as np
import matplotlib.pyplot as plot

class Test(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def test(self):
        fnx = lambda : np.random.randint(5, 50, 10)
        y = np.row_stack((fnx(), fnx(), fnx()))
        x = np.arange(10)
        
        y1, y2, y3 = fnx(), fnx(), fnx()
        
        fig = plot.figure()
        ax = fig.add_subplot(111)
        ax.stackplot(x, y)
        plot.show()
        
        fig = plot.figure()
        ax = fig.add_subplot(111)
        ax.stackplot(x, y1, y2, y3)
        plot.show()
        