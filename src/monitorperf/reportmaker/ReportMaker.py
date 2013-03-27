#encoding: utf-8
'''
Created on 15 janv. 2013

@author: guillaume
'''
import os
import urllib2
from PIL import Image as MImage
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import landscape


class ReportMaker(object):
    '''
    classdocs
    '''
    pathtoreport=""
    graphs=[]



    def __init__(self,reportfullpathname):
        '''
        Constructor
        '''
        self.pathtoreport=reportfullpathname

    
    
    def makeit(self):
        doc = SimpleDocTemplate(self.pathtoreport, pagesize=landscape(A4))
        style = getSampleStyleSheet()
        parts = []
        resizedimages=[]
        for n,p,t in self.graphs:
            resized=self.resizeImage(p)
            resizedimages.append(resized)
            parts.append(Paragraph(n,style["Heading1"]))
            parts.append(Image(resized))
            parts.append(Paragraph(t,style["Normal"]))
            parts.append(PageBreak())
        doc.build(parts)
        
        for i in resizedimages:
            os.remove(i)
        
    
    
    def get_python_image(self,filename):
        """ Get a python logo image for this example """
        if not os.path.exists(filename):
            response = urllib2.urlopen(
                'http://www.python.org/community/logos/python-logo.png')
            f = open(filename, 'w')
            f.write(response.read())
            f.close()
            
    def addGraph(self,graphpath, graphname, graphtext):
        self.graphs.append((graphname,graphpath,graphtext))
        
    def resizeImage(self,filename):
        img = MImage.open(filename)
        width, height = img.size
        MAXWIDTH=640.0
        if width>MAXWIDTH:
            
            factor=float(width/MAXWIDTH)
            newwidth=MAXWIDTH
            newheight=height/factor
            img2=img.resize((int(newwidth), int(newheight)), MImage.ANTIALIAS)
            img2.save(filename+"_resized","PNG")    
            return filename+"_resized"


if __name__ == '__main__':            

    
    c=ReportMaker("./python.pdf")
    c.get_python_image("python.png")
    c.addGraph("python.png", "Logo python", "Un magnifique logo python super beau")
    c.addGraph("python.png", "Logo python", "Un magnifique logo python super beau")
    c.addGraph("python.png", "Logo python", "Un magnifique logo python super beau")
    c.makeit()
    print "done!"

    #c.get_python_image()

    
    

        