from numpy import array
def saisirn():
    n=0  
    while not (2<=n<=40):
        n=int(input("donner n"))
    return n
###################
def verifch(ch):
    test=True
    for i in range(0,len(ch)):
        if not("A"<=ch[i].upper()<="Z"):
            test=False
    return test
######################
def saisirm():
    m=-1  
    while not(0<=m<=20):
        m=float(input("entrer un reel entre 0 et 20"))
    return m      
#######################
def remplir(t,n):
    for i in range(n):
        t[i]=dict()  #eleve
        t[i]["nom"]=input("donner votre nom")
        while not(verifch(t[i]["nom"])):
            t[i]["nom"]=input("donner votre nom")    
        t[i]["prenom"]=input("donner votre prenom")
        while not (verifch(t[i]["prenom"])):
            t[i]["prenom"]=input("donner votre prenom")
        t[i]["note"]=dict()  #note
        t[i]["note"]["ndc"]=saisirm()  #issm l module ili stha9ineh
        t[i]["note"]["nds"]=saisirm()
        t[i]["moy"]=(t[i]["note"]["ndc"]+2*t[i]["note"]["nds"])/3
###################
def affiche(t,n):
    for i in range(n):
        print(t[i]["nom"])
        print(t[i]["prenom"])
        print(t[i]["note"]["ndc"])
        print(t[i]["note"]["nds"])
        print(t[i]["moy"])
##################
def maxi(t,n):
    m=t[0]["moy"]
    for i in range(1,n):
        if t[i]["moy"]>m:
            m=t[i]["moy"]
    return m
####################
def affichemax(t,n):
    for i in range(n):
        if t[i]["moy"]==maxi(t,n):
            print("le premier de la classe est:",t[i]["nom"],t[i]["prenom"],t[i]["moy"])
################   
n=saisirn()
t=array([dict()]*n)
remplir(t,n)
affiche(t,n)
affichemax(t,n)

        
        
        
        
        
        
        
        