'''
Created on 27 mars 2013

@author: guillaume
'''
import os
import sys
import subprocess
import datetime

from monitorperf.utils.Utils import Utils
from monitorperf.Main import main 

from yaml import load, Loader

##########################################################################################################################################
# A LIRE AVANT DE LANCER
##########################################################################################################################################
# Sur un repertoire contenant des logs
# python -m SimpleHTTPServer 8000
# + revoir la conf en fonction
##########################################################################################################################################

##########################################################################################################################################
#   POUR LANCER EN LIGNE DE COMMANDE 
##########################################################################################################################################
# export PYTHONPATH=/home/guillaume/git/sandbox/src
##########################################################################################################################################

if __name__ == '__main__':
    f=None
    
    start_launcher=datetime.datetime.now()
    
    try:
        ####################
        #recuperer la conf
        ####################    
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

        f=open(confpath,'r')  
        settings=load(f, Loader=Loader)
        
        ###################################
        # pour tous les elements de la conf
        ###################################
        
        utils=Utils()
        
        for key in settings['targets'].keys():
            print key+': download'
            
            #wget files
            
            files=[]
            for i,url in enumerate(settings['targets'][key]['urls']):
                files.append(utils.wget(url,key+str(i)+'_'))
            
            all_in_one_file='/tmp/monitorperf_'+key+'.log'
            
            if os.path.exists(all_in_one_file):
                os.remove(all_in_one_file)
            
            print key+': concat'
            
            #concat/sort files
            for to_concat in files:
                cmd_output = subprocess.check_call('cat '+to_concat+' >> '+all_in_one_file,shell=True)
                #delete tmp wget files
                os.remove(to_concat)
            
            print key+': sort'
                
            #sort file
            master_file='/tmp/monitorperf_'+key+'_sorted.log'
            utils.sort(all_in_one_file,master_file)
            #delete non sorted file
            os.remove(all_in_one_file)
        
            print key+': grep'
        
            #grep main file and create temporary files
            greped_files=[]
            for i,pattern in enumerate(settings['targets'][key]['focus_on_service']):
                #create a file label
                label=pattern
                if label.find('.*')<>-1:
                    label=label.replace('.*','ALL')

                destfile='/tmp/monitorperf_'+key+'_sorted_'+label+'.log'
                if (utils.grep(master_file,destfile,pattern)==0):
                    greped_files.append((label,destfile))
                else:
                    print "ERROR: grep failed"
                
            #launch Main
            
            # for each temporary file => launch graph generator
            for label,greped_file in greped_files:
                finallabel=key+'_'+label
                print finallabel,': ',greped_file
             
                #cretaion des repertoires si ils n'existent pas
                if not os.path.exists(settings['targets'][key]['report_dir']):
                    os.mkdir(settings['targets'][key]['report_dir'])
                    
                if not os.path.exists(settings['targets'][key]['png_dir']):
                    os.mkdir(settings['targets'][key]['png_dir'])
             
                #definition du nom de sauvegarde du rapport
                timestring=str(datetime.datetime.today().strftime('%Y%m%d_%H%M%S_'))                
                reportfullname=timestring+'_'+finallabel+'_report.pdf'
                reportfullpath=os.path.join(settings['targets'][key]['report_dir'],reportfullname)
                
                #top de debut
                start=datetime.datetime.now()
                
                #generation du rapport
                main(greped_file,settings['targets'][key]['png_dir'],reportfullpath,finallabel,start)

        end_launcher=datetime.datetime.now()
        
            
        delta=end_launcher-start_launcher
    
        print('')
        print('*********************************************************')
        print('Launcher ALL JOBS DONE  in '+str(delta)+' !!!!')
        print('*********************************************************')
    

    finally:
        if f!=None:
            f.close()