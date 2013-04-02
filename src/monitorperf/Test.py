#encoding: utf-8
'''
Created on 27 mars 2013

@author: guillaume
'''
import matplotlib.pyplot as plt
import numpy as np
import datetime


#preuve que Matplot gère l'interpolation comme un grand
def interpolation():
    x = ['090001', '090002', '090003','090004','090005', '090006', '090007','090008', '090009','090010']
    #x = [1,2,3,4,5,6,7,8,9,10]
    y = [10,5,10,5,10,5,10,5,10,5]
    
    missing_data_x = ['090001','090003','090004','090005','090008','090010']
    #missing_data_x = [1,3,4,5,8,10]
    missing_data_y = [2,4,2,4,2,4]
    
    
    #check if x increase
    #print np.all(np.diff(x) > 0)

    res=np.interp(x, missing_data_x, missing_data_y)
    print res    
    plt.plot(x, y, 'b-')
    plt.plot(missing_data_x, missing_data_y, 'r-')
    plt.plot(x, res, 'g-')
    plt.show()    


if __name__ == '__main__':
    print str(datetime.datetime.today().strftime('%Y%m%d-%H%M%S'))
    
    print bool(None)
    print bool(0.5)
    print bool(0)
    print bool(1)


    y=[1,2,3,4,5,2,7,2,9,10]






    timedata=['10:58:26,181',
    '10:58:28,846',
    '10:58:30,361',
    '10:58:33,280',
    '10:58:40,085',
    '10:58:56,409',
    '10:59:01,610',
    '10:59:04,327',
    '10:59:06,759',
    '10:59:08,987']
    
    timedata_dot=['10:58:26.181',
    '10:58:28.846',
    '10:58:30.361',
    '10:58:33.280',
    '10:58:40.085',
    '10:58:56.409',
    '10:59:01.610',
    '10:59:04.327',
    '10:59:06.759',
    '10:59:08.987']
    print timedata
    print timedata_dot  
    
    x=[]
    for tt in timedata:
        receivedTime = datetime.datetime.strptime(tt, "%H:%M:%S,%f")
        x.append(receivedTime)
    
    plt.xticks(rotation=45,fontsize="small")
    plt.plot(x, y, 'b-')

    plt.show()        
    
   
    pass