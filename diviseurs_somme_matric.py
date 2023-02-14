#import
from numpy import array
from random import randint
"""
Algo modulaire
    Debut
"""
"""
Remplissage du matrice
"""
#saisir ; controlleé
def saisir(name):
    x=0
    while not 0<x<=7 :
        x=int(input("Donner le nombre de "+name+": "))
    return x
#remplir ; aléatoire
def remplir_matrice(l,c):
    for i in range(l):
        for j in range(c):
            M[i,j]=randint(-10,10)
"""
fonctions des sommes & diviseur ; 
calcul_affich_somme_positifs ; 
calcul_affich_somme_pairs ;
diviseur ;
"""
#calcul_affich_somme_positifs ;
def calcul_affich_somme_positifs():
    S=0
    for z in range(l):
        for w in range(c):
            if M[z,w]>=0:
                S+=M[z,w]
    print("Le somme des entiers positifs est :",S)
#calcul_affich_somme_pairs ;
def calcul_affich_somme_pairs():
    P=0
    for k in range(l):
        for o in range(c):
            if M[k,o]%2==0 :
                P+=M[k,o]
    print("Le somme des entiers pairs est :",P)
#diviseur ;
def diviseur(S):
    for f in range(l):
        for g in range(c):
            if (S%M[f,g])==0:
                print(M[f,g]," divise ",S)
"""
Algo Principale
"""
name="lignes"
l=saisir(name)
name="colonnes"
c=saisir(name)
M=array([[float]*c]*l)
remplir_matrice(l,c)
S=calcul_affich_somme_positifs()
P=calcul_affich_somme_pairs()
diviseur(S)