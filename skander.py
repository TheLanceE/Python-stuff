from numpy import *
def saisie():
    N=0
    while not(5<=N<=10):
        N=int(input("Saisie N :"))
    return N
def remplir_trie(T,N):
    T[0]=int(input("Case Numero 0 : "))
    while not (10<=T[0]<=99):
        T[0]=int(input("Case Numero 0 : "))
    for i in range(1,N):
        T[i]=int(input("Case Numero T["+str(i)+"]"))
        while not ((10<=T[i]<=99)and(T[i]>T[i-1])):
            T[i]=int(input("Case Numero T["+str(i)+"]"))
def rech_seq(T,N,X):
    j=0
    p=-1
    while (p==-1)and(j<=N-1):
        if T[j]==X:
            p=j
        else:
            j=j+1
    return p
def rech_dich(T,N,X):
    D=0
    F=N-1
    test=False
    while (test==False)and(D<=F):
        M=(D+F)//2
        if X==T[M]:
            test=True
        elif X>T[M]:
            D=M+1
        else:
            F=M-1
    return test
#pgpp
N=saisie()
T=array([int]*N)
remplir_trie(T,N)
X=int(input("Saisir la valeur à chercher : "))
choix=input("Saisir votre choix de Recherche S/D :")
if choix=="S":
    pos=rech_seq(T,N,X)
    if pos!=-1:
        print(X,"existe à la position",pos)
    else:
        print(X,"n'existe pas")
else:
    ok=rech_dich(T,N,X)
    if ok:
        print(X,"existe")
    else:
        print(X,"n'existe pas")