from numpy import array
#saisir ; controleé
def saisir():
    N=0
    while not (5<=N<=30):
        N=int(input("Donner le taille du tableau"))
    return N
#remplir ; condition distincs
def remplir(T,N):
    for i in range(N):
        T[i]=int(input("Donner l'element T["+str(i)+"]"))
        while not (T[i]>0 and T[i] in range(1,99)):
             for j in range(N):
                if T[i]==T[j]:
                    print("L'element existe déja dans le tableau !")
                else:
                    T[i]=int(input("Donner l'element T["+str(i)+"]"))
#trier
def tri_crsnt(T,T1,N):
    for j in range(N):
        x=T[j]
        T1[x]=x
    z=1
    for k in range(1,100):
        if T1[k]!=0:
            T[z]=T1[k]
            z=z+1
#affich
def affich(X,N):
    for i in range(N):
        print("La case numero [",i,"] : ",T[i],end="|")
#pgpp
N=saisir()
T=array([int]*N)
remplir(T,N)
affich(T,N)
T1=array([0]*99)
tri_crsnt(T,T1,N)
affich(T1,N)