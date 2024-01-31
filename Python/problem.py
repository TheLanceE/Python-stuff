from numpy import *
from pickle import *
def saisir():
    F=open("journal.dat",ab)
    valide=False
    while not valide:
        j=dict()
        j["num"]=int(input("Donner un numero"))
        j["titre"]=input("donner un titre")
        j["periode"]=input("Donner le periode")
        while not(j["periode"] in ["O","H","M","A","Q","T"]):
            j["periode"]=input("Donner le periode")
        j["spé"]=input("Donner votre specialité")
        while not(j["spé"] in ["Economique","Culturelle","Sportif"]):
            j["spé"]=input("Donner votre specialité")
        j["prix"]=int(input("Donner le prix"))
        dumb(j,F)
        choix=input("vous pouvez entrez une autre choix")
        if choix=="non":
            valide=True
    F.close()
def afficher():
    p=input("Donner la periode")
    while not(p in ["O","H","M","A","Q","T"]):
        p=input("Donner la periode")
    F=open("journal.dat","rb")
    fin_fichier=False
    while fin_fichier==False:
        try:
            j=load(F)
            if j['periode']==p:
                print(j)
        except :
            fin_fichier=True
    F.close()
def chercher():
    nom=input("donner le titre de journaux")
    F=open("journal.dat","rb")
    fin_fichier=False
    while not(fin_fichier):
        try:
            j=load(F)
            if nom in j["titre"]:
                print(j)
        except :
            fin_fichier=True
    F.close()