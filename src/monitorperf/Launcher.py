'''
Created on 27 mars 2013

@author: guillaume
'''
import os
import sys
from yaml import load, Loader


def wget(url,label):
    filename=''
    pass
    return filename

def grep(source_file,pattern,filename):
    pass

if __name__ == '__main__':
    f=None
    try:
        ####################
        #recuperer la conf
        ####################    
        fullpath=os.path.join(os.getcwd(),sys.argv[0])
    
        pathelements=[]
        pathelements=fullpath.split("/")
        #supprimer le nom du .py du path
        del list[-1]

        res="/"
        for e in pathelements:
            res=os.path.join(res,e)
        
        confpath=os.path.join(res,'../../ressources/monitorperf/conf/configuration.yaml')
        print confpath

        f=open(confpath,'r')  
        settings=load(f, Loader=Loader)
        
        ###################################
        # pour tous les elements de la conf
        ###################################
        
        for key in settings.keys():
            print settings[key]
            
            #wget files
            files=[]
            for i,url in enumerate(settings[key]['urls']):
                files.append(wget(url,i))
                
                
            #concat/sort files
            #resultat=key.log 
            source_file=key+'.log'
    
    
    
            #delete tmp wget files
            
            
            #grep main file and create temporary files
    
            greped_files=[]
            for i,pattern in enumerate(settings[key]['focus_on_service']):
                greped_files.append(pattern,grep(source_file,pattern,i))
            #launch Main
            
            print greped_files
            
            # for each temporary file => launch graph generator
            for pattern,greped_file in greped_files:
                if pattern=='*':
                    pattern='ALL'
                print key,'_',pattern,'_',greped_file
                pass
            
    
        print settings['ARK']
    finally:
        if f!=None:
            f.close()