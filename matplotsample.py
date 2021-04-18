from matplotlib.pyplot import *
import numpy as np
from math import *

def func_plotter():
    x=np.linspace(-1,2000,100)
    y=6.19380059632563*x+0.9783868485067422 

    plot(x,y)




def file_drawer():
    f=open('tcs.txt','r')             #enter the filename
    f.readline()[:-1]
    x1=[]
    y1=[]
    while(1):
        text=f.readline()
        if 'eof' in text:
            break;
        xr,yr=text.split(',')
        x1.append(float(xr))
        y1.append(float(yr))
    
    scatter(x1,y1)
    
    

func_plotter()
file_drawer()



show()
