from pickle import dump,load
from numpy import array
def remplir():
    global n
    n=0
    f=open("nombre1.dat","wb")
    v="O"
    while(v.upper()=="O" and n<100):
        x=int(input("x= "))
        dump(x,f)
        v=input("vouler vous ajouter un nombre: ")
        while not(v.upper()=="O" or v.upper()=="N"):
            v=input("vouler vous ajouter un nombre: ") 
        n=n+1
    f.close()
def remplir2():
    f=open("nombre1.dat","rb")
    for i in range(n):
        t[i]=load(f)
    f.close()
def remplir3():
    g=open("nombre2.dat","wb")
    for i in range(n):
        dump(t[i],g)
    g.close
remplir()
t=array([int()]*n)
remplir2()
remplir3()