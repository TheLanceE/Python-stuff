from pickle import *
def saisir():
    n=int(input("Donner le taille du fichier : "))
    while not(2<=n<=10):
        n=int(input("Donner le taille du fichier : "))
    return n
def remplir1(n):
    f1=open("nb_base.dat","wb")
    for i in range(n):
        ch=input("Ecrire une chaine a remplir : ")
        while not(verif(ch)):
            ch=input("Ecrire une chaine a remplir : ")
        dump(ch,f1)
def verif(ch):
    i=0
    while (i<len(ch) and ("0"<=ch[i]<="9" or "A"<=ch[i]<="F")):
        i=i+1
    return (i==len(ch) and len(ch)<=5)
def remplir2(n):
    f1=open("nb_base.dat","rb")
    f2=open("nombre.txt","w")
    for i in range(n):
        ch=load(f1)
        b=nb_base(ch)
        nb=convB10(ch,b)
        chs="("+ch+")"+str(b)+"=("+str(nb)+")10"
        f2.write(chs+"\n")
    f1.close()
    f2.close()
def nb_base(ch):
    maxi=ch[0]
    for i in range(1,len(ch)):
        if ch[i]>maxi:
            maxi=ch[i]
    if "0"<=maxi<="9":
        return (int(maxi)+1)
    else:
        return(ord(maxi)-54)
def afficher(n):
    f2=open("nombre.txt","r")
    for i in range(n):
        ch=f2.readline()
        print(ch)
    f2.close()
def convB10(ch,b):
    n=0
    p=1
    for i in range(len(ch)-1,-1,-1):
        if "0"<=ch[i]<="9":
            n=n+int(ch[i])*p
        else:
            n=n+(ord(ch[i])-55)*p
        p=p*b
    return n
        
#pp
n=saisir()
remplir1(n)
remplir2(n)
afficher(n)