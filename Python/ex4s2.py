from array import*
n=int(input("Donner le taille de la liste des valeurs : "))
s=0
Tn=array([0]*n)
for i in range(n):
    Tn[i]=int(input("Donne le valeur de Tn[",i,"]"))
    s=Tn[i]+s