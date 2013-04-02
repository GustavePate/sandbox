#encoding: utf-8
'''
Created on 11 oct. 2012

@author: guillaume
'''
from monitorperf.utils.MyConfiguration import Configuration
from monitorperf.filter.Filter import Filter


def filtr(func):
    res=func
    filtr=Filter()
    if res>filtr.getGlobalcutoff():
        res=filtr.getGlobalcutoff()
    return float(res)

class Mesure(object):


    text=""
    date=""
    heure=""
    fields=[]
    globalresponsetime=0.0
    

    def __init__(self,text):
        '''
        Constructor
        '''
        self.text=text
        self.fields=self.text.split(";")
        self.star=self.text.split("*")
        for f in self.fields:
            f.strip()
        for f in self.star:
            f.strip()


    def __str__(self):
        #return '{0:53} {1:10} {2:10} {3:.5f} {4:10} {5:8}'.format(self.getNom(),self.getRealSize(),self.getSize(), self.getRealAge(),self.getAge(),self.getDate())
        res=""
        for f in self.fields:
            res=res+f
            
        return res
        #return 'mesure:{0:53}'.format(self.text)
    
    

    
    def getServiceName(self):
        return self.fields[4] 
    
    def getDate(self):
        return self.fields[1]
    
    def getTime(self):
        return self.fields[2] 
        
    def getFunctionalData(self):
        return self.fields[5]
    
    #@filtr  
    def getGlobalResponseTime(self):
        try:
            if self.globalresponsetime>0:
                res=self.globalresponsetime
            else:
                res=float(self.fields[6].split(":")[1].strip())
            return  float(res)
        except:
            Configuration.getLogger().info("getGlobalResponseTime"+self.text)
            return 20000
    
    def setGlobalResponseTime(self,grt):
        self.globalresponsetime=grt
        
    #@filtr                      
    def getSPCResponseTime(self):
        try:
            res=self.fields[7]
            if self.fields[7].find('*')<>-1:
                res=self.fields[7].split('*')[0]
            res=float(res.split(":")[1].strip())
    
            return res
        except:
            Configuration.getLogger().info("getSPCResponseTime"+self.text)
            return 20000
    
    def getRecifResponseTime(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("recif;")<>-1:
                    detail=f.split(";")
                    res=float(detail[3].split(":")[1])
        return res

    def getRecifCallNumber(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("recif;")<>-1:
                    detail=f.split(";")
                    res=int(detail[1].split(":")[1])
        
        return res
    
    def getRecifTRResponseTime(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("recif_tr;")<>-1:
                    detail=f.split(";")
                    res=float(detail[3].split(":")[1])
        return res

    def getRecifTRCallNumber(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("recif_tr;")<>-1:
                    detail=f.split(";")
                    res=int(detail[1].split(":")[1])
        
        return res
    
    
    def getHostResponseTime(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("host;")<>-1:
                    detail=f.split(";")
                    res=float(detail[3].split(":")[1])
        return res

    def getHostCallNumber(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("host;")<>-1:
                    detail=f.split(";")
                    res=int(detail[1].split(":")[1])
        
        return res

    def getPacmanResponseTime(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("pacman;")<>-1:
                    detail=f.split(";")
                    res=float(detail[3].split(":")[1])
        return res

    def getPacmanCallNumber(self):
        res=None
        for i, f in enumerate(self.star):
            if i>0:
                if f.find("pacman;")<>-1:
                    detail=f.split(";")
                    res=int(detail[1].split(":")[1])
        
        return res
        
        