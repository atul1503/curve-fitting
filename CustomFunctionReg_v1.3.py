from math import *

def LinearRegressor(data,d,deg):
    degree=deg
    w=[1]*(degree)
    dw=[0]*len(w)
    mvp=0
    maxe=float(input('Enter the max error : '))
    e=maxe+50
    it=float(input('Enter the iterations: '))
    damp_decay=float(input('Enter the Damping Decay: '))
    
    try:
        q=open('weights.txt','r')
        u=q.readline().split(',')
        for i in range(len(w)):
            w[i]=float(u[i])
        
        u=q.readline().split(',')
        for i in range(len(dw)):
            dw[i]=float(u[i])
            
        q.close()
    except:
        pass
    
        
        
    i=0
    i=int(i)
    while i<=it and (e>maxe or e<-maxe):
                
        e=0
        for j in range(len(data)):    
                     
                     
            x=data[j][mvp]
            
            
            
            
            
            #Customize your function here 
            
            pred=w[0]*sin(w[1]*x+w[2])+w[3]*x+w[4]

            
            #Customization ends here
            
            
            
            
            
            e=e+pred-data[j][-1]
            
            
            pre=d*(pred-data[j][-1])
            
            
            
            
            #Customize derivatives from here
            
            dw[0]=pre*sin(w[1]*x+w[2])
            dw[1]=pre*w[0]*x*cos((w[1]*x)+w[2])
            dw[2]=pre*w[0]*cos((w[1]*x)+w[2])
            dw[3]=pre*x
            dw[4]=pre*1
            
            
            
            #Customization ends here
            
            
            
            
            
                    
            for k in range(len(w)):
                w[k]=w[k]-dw[k]        
            
            
            
                    
        i=int(i)
        
        if i%10000==0 and 'nan' not in str(w):
            g=open('results.txt','a')
            pgl=str(w)+str(e)+'\n'
            g.write(pgl)
            g.close()
            h=open('weights.txt','w')
    
            for y in w:
                if  y!=nan:
                    h.write(str(y)+',')
                    
            h.write('\n')
            for der in dw:
                if der!=nan:
                    h.write(str(der)+',')
    
            h.close()
            
            
            
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
    deg=int(input('Enter no. of coefficients: '))
    d=float(input('Enter the Damping Coefficient: '))
    print()
    wt,e=LinearRegressor(data,d,deg)
    print('\n\n')
    print('The best fitted function coefficients are: ',end='')
    print(wt,'\nError:',e)
    input()
    
    
main()