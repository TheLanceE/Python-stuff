from numpy import array
def saisie():
    n=int(input("N="))
    while not 2<=n<=40:
        n=int(input("N="))
    return n
def verifch(ch):
    i=0
    while (i<len(ch) and "A"<=ch[i].upper()<="Z"):
        i+=1
    return i>=len(ch)
def remplir(n):
    for i in range(n):
        t[i]=dict()
        t[i]["nom"]=input("Donner le nom d'eleve n: ")
        while not verifch(t[i]["nom"]):
            t[i]["nom"]=input("Donner le nom d'eleve n: ")
        t[i]["prenom"]=input("Donner le prenom d'eleve n: ")
        while not verifch(t[i]["prenom"]):
            t[i]["prenom"]=input("Donner le prenom d'eleve n: ")
        e=dict()
        e["ndc"]=float(input("Donner le ndc: "))
        while not 0<=e["ndc"]<=20:
            e["ndc"]=float(input("Donner le ndc: "))
        e["nds"]=float(input("Donner le nds: "))
        while not 0<=e["nds"]<=20:
            e["nds"]=float(input("Donner le nds: "))
        t[i]["note"]=e
        t[i]["moy"]=(t[i]["note"]["ndc"]+2*t[i]["note"]["nds"])/3
def maxmoy(n):
    max=t[0]["moy"]
    for i in range(1,n):
        if t[i]["moy"]>max:
            max=t[i]["moy"]
    return max
def affiche(n):
    for i in range(n):
        print(t[i]["nom"],t[i]["prenom"],t[i]["note"]["ndc"],t[i]["note"]["nds"],t[i]["moy"])
        print()
        if t[i]["moy"]==maxmoy(n):
            print("le(a) premier(e) est",t[i]["nom"],t[i]["prenom"],t[i]["moy"])
n=saisie()
t=array([dict()]*n)
remplir(n)
affiche(n)