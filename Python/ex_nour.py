from pickle import*
from numpy import array
def taille():
    f=open("source.txt","r")
    n=0
    ch=f.readline()
    while not ch!="":
        ch=f.readline()
        n=n+1
    f.close()
    return n
def tansfert(f,m,n):
    f=open("source.txt","a")
    for i in range(n):
        ch=f.readline()
        ch=ch[0,len(ch)] 
        ch=ch+" "
        for j in range(0,9):
            p=pos(" ",ch)
            a=ch[0,p]
            m[i,j]=int(a)
            ch=ch[p,len(ch)] 
    f.close()
def tri(n,t):
    for i in range(n-1):
        for j in range(n):
            if t[i]>t[j]:
                aux=t[i]
                t[i]=t[j]
                t[j]=aux
def traimtment(m,R,n):
    for i in range(0,9):
            t[i]=m[i,j]
    tri(t,n)
    for j in range(n):
        m[i,j]=t[i]
    R=open("source.txt","w")
    for i in range(n):
        for j in range(0,9):
            ch=ch+str(m[i,j]+" ")
        ch=ch[0,len(ch)]
        R.write(ch+"/nl")
    R.close()  
def affi(R):    
    R=open("source.txt","r")
    while not ch!="":
        ch=R.readline()
        R.write(ch)
    R.close()
#pp
n=taille()
t=array([[int()]*m]*n)
tansfert(f,m,n)
traimtment(m,R,n)
affi(R)