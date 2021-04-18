from math import *


weights=5

def custom(x,w):
    return w[0]*sin(w[1]*x+w[2])+w[3]*x+w[4]
    
    
    
    
    
def par_deriv(y,x,w,k,d):
    original=float(w[k])
    if direction(y,x,d,w,k)==1:
        w[k]=w[k]+d/2
        prior=custom(x,w)
        w[k]=original
        later=custom(x,w)
        return (abs(prior-later)*2)/d
    elif direction(y,x,d,w,k)==-1:
        w[k]=w[k]-d/2
        prior=custom(x,w)
        w[k]=original
        later=custom(x,w)
        return (abs(prior-later)*2)/(-d)
    else:
        return 0
        

def direction(y,x,d,w,k):
    original=float(w[k])
    final=0
    w[k]=original+d
    pos=y-custom(x,w)
    w[k]=original-d
    neg=y-custom(x,w)
    w[k]=original
    if abs(pos)<abs(neg):
        final=1
    elif abs(neg)<abs(pos):
        final=-1
    else:
        final=0
    
    return final
    
    





def LinearRegressor(data,d):
    w=[0.01]*weights
    mvp=0
    e=1e+100
    maxe=float(input('Enter the max error: '))
    it=float(input('Enter the iterations: '))
    
    i=0
    while i<it and abs(e)>maxe:
        e=0
        j=0
        while j<len(data):
            x=data[j][mvp]
            y=data[j][-1]
            pred=custom(x,w)
            e=e+(y-pred)
            k=0
            while k<len(w):
                w[k]=w[k]+direction(y,x,d,w,k)*d*(y-pred)*par_deriv(y,x,w,k,d)
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