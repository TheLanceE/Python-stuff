date = {"J":int(), "M": int(),"A":int()}
Etudiant = {"Mat":str(),"Nom":str(),"PRN":str(),"DN":date,"N1":float(),"N2":float(),"Mg":float()}
from numpy import array
def saisie():
    N=int(input("Saisir nombre d'etudiants :"))
    while not(3<=N<=100):
        print("Unvalid! donnez un nombre entre 3 et 100")
        N=int(input("Saisir nombre d'etudiants :"))
    return N
def remplir(T,N):
    for i in range(N):
        T[i]={}
        T[i]["DN"]={}
        T[i]["Mat"]=input("Taper votre matricule :")
        while not ("A"<=T[i]["Mat"][0]<="Z")or(T[i]["Mat"][1:].isdigit()==False)or(len(T[i]["Mat"][1:]!=3)):
            T[i]["Mat"]=input("Taper votre matricule :")
            T[i]["Nom"]=input("Taper le prénom: ")
            T[i]["DN"]["J"]=int(input("Taper le jour :"))
            while not (1<=T[i]["DN"]["J"]<=31):
                T[i]["DN"]["J"]=int(input("Taper le jour :"))
            T[i]["DN"]["M"]=int(input("Taper le mois :"))
            while not (1<=T[i]["DN"]["M"]<=12):
                T[i]["DN"]["M"]=int(input("Taper le mois :"))
            T[i]["DN"]["A"]=int(input("Tape l'anneé :"))
            while not (1000<=T[i]["DN"]["A"]<=9999):
                T[i]["DN"]["A"]=int(input("Tape l'anneé :"))
            T[i]["N1"]=float(input("Taper la note1 :"))
            T[i]["N2"]=float(input("Tape la note2 :"))
            T[i]["Mg"]=(T[i]["N1"]+T[i]["N2"])/2
def calcul(T,N):
    M=0
    for i in range(N):
        M=M+T[i]["Mg"]
    return round(M/N,2)
def affiche(T,N):
    for j in range(N):
        if T[j]["Mg"]>=10:
            print('Matricule',T[j]["Mat"])
            print('Nom',T[j]["Nom"])
            print('Prenom',T[j]["PRN"])
            print('Date',T[j]["DN"]["J"],"/",T[j]["DN"]["M"],"/",T[j]["DN"]["A"])
def meilleur(T,N):
    Max=T[0]["Mg"]
    for k in range(1,N):
        if T[k]["Mg"]>Max:
            Max=T[k]["Mg"]
    return Max
def afficher_major(T,N):
    Mx=Meilleur(T,N)
    for h in range(N):
        if T[h]["Mg"]==Mx:
            print('Matricule',T[h]["Mat"])
            print('Nom',T[h]["Nom"])
            print('Prenom',T[h]["PRN"])
            print('Date',T[h]["DN"]["J"],"/",T[h]["DN"]["M"],"/",T[h]["DN"]["A"])
def saisirMat():
    Mt=input("Saisir la matricule de l'etudiant a chercher")
    return Mt
def recherche(T,N,Mt):
    k=0
    test=False
    while (k<N) and (test==False):
        if T[k]["Mat"]==Mt:
            test=True
        else:
            k=k+1
    if test:
        print('Matricule',T[k]["Mat"])
        print('Nom',T[k]["Nom"])
        print('Prenom',T[k]["PRN"])
        print('Date',T[k]["DN"]["J"],"/",T[k]["DN"]["M"],"/",T[k]["DN"]["A"])
    else:
        print("Etudiant introuvalbe")
#pgpp
N=saisie()
T=array([Etudiant]*N)
remplir(T,N)
M1=calcul(T,N)
print("moyenne generale de la section=",M1)
affiche(T,N)
afficher_major(T,N)
Mt=saisirmat()
recherche(T,N,Mt)