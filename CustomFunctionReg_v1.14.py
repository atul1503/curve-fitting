from math import *


weights=2

def custom(x,w):
    return w[0]*x+w[1]
    
def ActualCall():
    #d=Damping Coefficient;for loading previous results,use the previous d for proper resumption.
    #maxe=Max Error after which the search stops
    #it=Iterations
    #lookup=Lookup multiplier
    #interval=Save interval iteration number
    #load=Load params from file
    #signChangeStop=Whether to stop when error sign changes.
    #writeToAnyFile=Whether to write weights,errors to any file(it can be backup,parameters or signChangeSnapshot)
    #speed=whether the damping coeffcient should increase to maintain speed or not.
    #accelerator=multiplier at which d will increase if the error slope slows down while optimization.
    #slowIndicator=if current error is more than slowIndicator*previousError then error slope is slow. 
    
    d=2.45e-7
    fileName='tcs.txt'
    it=1e7
    lookup=1
    interval=10
    maxe=2
    speed=1
    accelerator=1+1e-6
    slowIndicator=1-1e-2
    signChangeStop=1
    writeToAnyFile=1
    load=1
    
    
    data,attr=readData(fileName)
    print()
    return LinearRegressor(data,d,maxe,it,lookup,interval,load,speed,signChangeStop,writeToAnyFile,accelerator,slowIndicator)
    


def signCheck(x,y):
    if x>0 and y>0:
        return 1
    elif x<0 and y<0:
        return 1
    else:
        return 0



def speedify(d,e,pe,acc,slowIndicator):
    if e/(pe*slowIndicator)>1 and abs(e)<=abs(pe) and signCheck(e,pe):
        return d*acc
    return d

    
    
    
def par_deriv(y,x,w,k,lookup,d):
    original=float(w[k])
    direction_ref=direction(y,x,lookup,d,w,k)
    if direction_ref==1:
        w[k]=w[k]+d
        prior=custom(x,w)
        w[k]=original
        later=custom(x,w)
        return abs(prior-later)/d
    elif direction_ref==-1:
        w[k]=w[k]-d
        prior=custom(x,w)
        w[k]=original
        later=custom(x,w)
        return abs(prior-later)/(-d)
    else:
        return 0
        

def direction(y,x,lookup,d,w,k):
    original=float(w[k])
    final=0
    w[k]=original+d*lookup
    pos=y-custom(x,w)
    w[k]=original-d*lookup
    neg=y-custom(x,w)
    w[k]=original
    if abs(pos)<abs(neg):
        final=1
    elif abs(neg)<abs(pos):
        final=-1
    elif abs(neg)==abs(pos):
        final=0
        
    return final
    

                
                








def LinearRegressor(data,d,maxe,it=1e7,lookup=1,interval=1000,load=0,speed=0,signChangeStop=1,writeToAnyFile=1,acc=1.01,slowIndicator=0.99):
    w=[0.01]*weights
    mvp=0
    flag=0
    e=1e+100
    first=0
    second=0
    backup=1e+101
    if load:
        f=open('parameters.txt','r')
        w=f.readline().split()
        w=[float(n) for n in w]
        f.close()
    
    i=0
    i=int(i)
    while i<it and abs(e)>maxe:
        if int(i)%interval==0 and int(i)!=0:
            print('Error=',e,' and d=',d)
            if speed:
                if first:
                    d=speedify(d,e,pe,acc,slowIndicator)
                first=1
                pe=float(e)
                
        if int(i)%interval==0 and int(i)!=0 and writeToAnyFile:
            f=open('parameters.txt','w')
            for j in w:
                f.write(str(j)+' ')
            f.write('\n'+'Error='+str(e)+' and '+'Damping Coefficient='+str(d)+' at iteration='+str(i)+'\n')
            f.close()
            if abs(e)<abs(backup):
                g=open('backup.txt','w')
                for j in w:
                    g.write(str(j)+' ')
                g.write('\n'+'Error='+str(e)+' and '+'Damping Coefficient='+str(d)+' at iteration='+str(i)+'\n')
                backup=float(abs(e))
                g.close()
            if signChangeStop:
                if second and signCheck(prevE,e)==0:
                    g=open('parameters.txt','w')
                    for j in prevW:
                        g.write(str(j)+' ')
                    g.write('\n'+'Error='+str(prevE)+' and '+'Damping Coefficient='+str(d)+' at iteration='+str(i)+'\n')
                    g.close()
                    g=open('signChangeSnapshot.txt','w')
                    for j in prevW:
                        g.write(str(j)+' ')
                    g.write('\n'+'Error='+str(prevE)+' and '+'Damping Coefficient='+str(d)+' at iteration='+str(i)+'\n')
                    g.close()
                    print('Error sign changed! Snapshot saved to file.Go check it out!')
                    input()
                    exit()
                second=1
                prevE=float(e)
                prevW=[i for i in w]
            
            
            
        
            
            
            
            
        
        e=0
        j=0
        while j<len(data):
            x=data[j][mvp]
            y=data[j][-1]
            pred=custom(x,w)
            e=e+(y-pred)
            k=0
            while k<len(w):
                w[k]=w[k]+direction(y,x,lookup,d,w,k)*d*(y-pred)*par_deriv(y,x,w,k,lookup,d)
                k=k+1
                
            j=j+1
            
        i=i+1
        
    g=open('backup.txt','w')
    for j in w:
        g.write(str(j)+' ')
    g.write('\n'+'Error='+str(e)+' and '+'Damping Coefficient='+str(d)+' at iteration='+str(i)+'\n')
    g.close()
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
    wt,e=ActualCall()
    print('\n\n')
    print('The best fitted function coefficients are: ',end='')
    print(*wt)
    print('With error :',e)
    input()
    
    
main()