client={ "Num":str(),"Sol":int() }
ooredoo={ "OC":client, "Spair":int(), "Simp":int()}
from numpy import array
"""
Algo Modulaire
    Debut
"""
#Saisir nombre client
def saisir():
    N=int(input("Donner le nombre de clients: "))
    while not 5<=N<=200:
        print("Invalid! saisir un nombre entre 5 et 200!")
        N=int(input("Donner le nombre de clients: "))
    return N
#Remplir T par numero telephone
def remplir(T,N):
    for i in range(N):
        T[i]={}
        T[i]["Num"]=input("Donner votre numéro :")
        while not (len(T[i]["Num"])==8)and(T[i]["Num"].isdigit()==True):
            T[i]["Num"]=input("Donner votre numéro :")
        T[i]["Sol"]=int(input("Donner votre solde :"))
        while not (0<=T[i]["Sol"]):
            T[i]["Sol"]=int(input("Donner votre solde :"))
#Remplir R
def transfer(R,T,N):
    for j in range(N):
        R[j]={}
        R[j]["OC"]={}
        R[j]["OC"]["Num"]=T[j]["Num"]
        R[j]["Spair"]=SOMME_PAIR(T[j]["Num"])
        R[j]["Simp"]=SOMME_IMPAIR(T[j]["Num"])
        if R[j]["Spair"]>R[j]["Simp"]:
            R[j]["OC"]["Sol"]=T[j]["Sol"]+10
        else:
            R[j]["OC"]["Sol"]=T[j]["Sol"]
def SOMME_PAIR(x):
    xs=0
    for a in range(len(x)-1):
        if int(x[a])%2==0:
            xs=int(x[a])+xs
    return xs
def SOMME_IMPAIR(y):
    ys=0
    for b in range(len(y)-1):
        if int(y[b])%2!=0:
            ys=int(y[b])+ys
    return ys
#Affich; R
def affich(R,N):
    for p in range(N):
        print("Le numéro ",R[p]["Num"]," à ",R[p]["Sol"]," solde; Spair=",R[p]["Spair"]," Simp=",R[p]["Simp"])
"""
Fin
Programme Principale
Debut
"""
N=saisir()
T=array([client]*N)
remplir(T,N)
R=array([ooredoo]*N)
transfer(R,T,N)
affich(R,N)
"""
Fin
"""