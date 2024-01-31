from pickle import dump,load
def saisir():
    n=int(input("Donner N: "))
    while not( 2<=n<=10):
        n=int(input("Donner N: "))
    return n
def remplir(n):
    f=open("moy.dat","wb")
    for i in range(n):
        x=float(input("x= "))
        dump(x,f)
    f.close()
def afficher(n):
    f=open("moy.dat","rb")
    m=load(f)
    b=True
    while b:
        try:
            x=load(f)
            if x>m:
                m=x
        except:
            b=False
    print("max= ",m)
    f.close()

#
n=saisir()
remplir(n)
afficher(n)