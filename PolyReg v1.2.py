from math import *

def LinearRegressor(data,d,deg):
    degree=deg
    w=[0.01]*(degree+1)
    dw=[0]*len(w)
    mvp=0
    it=float(input('Enter the iterations: '))
    damp_decay=float(input('Enter the Damping Decay: '))
    
    
    
        
        
    i=0
    i=int(i)
    while i<=it:
                
        e=0
        for j in range(len(data)):    
                     
                     
            x=data[j][mvp]
            
            
            
            
            
            #Customize your function here 
            
            term=degree
            pred=0
            for k in range(len(w)):
                pred=pred+(x**term)*w[k]
                term=term-1

            
            #Customization ends here
            
            
            
            
            
            e=e+pred-data[j][-1]
            
            
            pre=d*(pred-data[j][-1])
            
            
            
            
            #Customize derivatives from here
            
            term=degree
            for k in range(len(w)):
            
                dw[k]=pre*(x**term)
                term=term-1
            
            
            
            #Customization ends here
            
            
            
            
            
                    
            for k in range(len(w)):
                w[k]=w[k]-dw[k]        
            
            
            
                    
        
            
            
        d=d/damp_decay   
        i=i+1
    
        
    print(pred,data[-1][-1],sep='   ')
    

    
    return w,e
    
def readData(fileName):
    f=open(fileName,'r')
    data=[]
    attr=f.readline().split(',')
    attr=attr[:-1]
    temp=f.readline()
    while 'eof' not in temp:
        temp=temp[:-1]
        ttemp=temp.split(',')
        data.append(ttemp)
        temp=f.readline()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=float(data[i][j])
    
    f.close()
    return data,attr    
    
def main():
    fileName=input('Enter the file name with path :')
    data,attr=readData(fileName)
    deg=int(input('Enter Degree of Polynomial: '))
    d=float(input('Enter the Damping Coefficient: '))
    print()
    wt,e=LinearRegressor(data,d,deg)
    print('\n\n')
    print('The best fitted function coefficients are: ',end='')
    print(wt,'\nError:',e)
    input()
    
    
main()