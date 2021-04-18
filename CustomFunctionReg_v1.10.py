from math import *


weights=2

def custom(x,w):
    return w[0]*x+w[1]
    
    
    
    
    
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
    else:
        final=0
        print('Local Minima!',w)
        input()
        exit()
    
    return final
    
    





def LinearRegressor(data,d):
    w=[0.01]*weights
    mvp=0
    e=1e+100
    backup=1e+101
    maxe=float(input('Enter the max error: '))
    it=float(input('Enter the iterations: '))
    lookup=float(input('Enter the lookup multiplier: '))
    interval=int(input('Enter the Save interval iteration number: '))
    load=int(input('Load params from file: '))
    if load:
        f=open('parameters.txt','r')
        w=f.readline().split()
        w=[float(n) for n in w]
        f.close()
    
    i=0
    i=int(i)
    while i<it and abs(e)>maxe:
        if int(i)%interval==0 and int(i)!=0:
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
    d=float(input('Enter the Damping Coefficient: '))
    print()
    wt,e=LinearRegressor(data,d)
    print('\n\n')
    print('The best fitted function coefficients are: ',end='')
    print(wt)
    print('With error :',e)
    input()
    
    
main()