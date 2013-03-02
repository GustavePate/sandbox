'''
Created on 27 oct. 2012

@author: guillaume
'''

import sys

import cairo

import pycha.pie

import pycha.line

class Chart(object):
    '''
    classdocs
    '''
    
    output = 'linechart.png'
    lines = (
             ('bar.py', 319),
             ('chart.py', 875),
             ('color.py', 204),
             ('line.py', 130),
             ('pie.py', 352),
             ('scatter.py', 38),
             ('stackedbar.py', 121),
             )



    def setData(self,data):
        self.lines = data
    
    def draw(self):
        self.lineChart(self.output)
    
    def lineChart(self,output):
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)
    
        dataSet = (
            ('lines', [(i, l[1]) for i, l in enumerate(self.lines)]),
            )
    
        options = {
            'axis': {
                'lineWidth':1.0,
                'lineColor':'#0f0000',
                'tickSize':3.0,
                'labelColor':'#666666',
                'labelFont':'Tahoma',
                'labelFontSize':9,
                'labelWidth':50.0,
                'tickFont':'Tahoma',
                'tickFontSize':9,
                'x': {
                    'hide':False,
                    'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(self.lines)],
                    #'ticks': None,
                    'tickCount':2,
                    'tickPrecision':1,
                    'range':None,
                    'rotate':90.0,
                    'label':None,
                    'interval':2,
                    'showLines':False,                    
                    
                },
                'y': {
                    'hide':False,
                    'ticks':None,
                    'tickCount':10,
                    'tickPrecision':1,
                    'range':None,
                    'rotate':None,
                    'label':None,
                    'interval':0,
                    'showLines':True,
                }
            },
            'background': {
                'color':'#eeeeff',
                'hide':False,
                'baseColor':None,
                'chartColor':'#f5f5f5',
                'lineColor': '#444444',
                'lineWidth':1.5,
            },
            'legend': {
                'hide': False,
                'borderWidth':1,
                'opacity':0.8,
                'borderColor':'#000000',
            },
            'yvals':{
                'show':True,
                'inside':True,
                'fontSize':11,
                'fontColor':'#000000',
                'skipSmallValues':True,
                'snapToOrigin':True,
                'renderer':None
            },
            'fillOpacity':0.2,
            'colorScheme': {
                'name': 'gradient',
                'args': {
                    'initialColor': 'blue',
                },
            },

            'title':'Mon Titre',
            'titleColor':'#000000',
            'titleFont':'Tahoma',
            'titleFontSize':12,
            'encoding':'utf-8',
     }
        chart = pycha.line.LineChart(surface, options)
    
        chart.addDataset(dataSet)
        chart.render()
    
        surface.write_to_png(output)
    
    

    def __init__(self,output):
        '''
        Constructor
        '''
        self.output=output
        #self.setData(data)

    