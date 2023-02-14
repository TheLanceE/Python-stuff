#saisir
CH=input("Donner une chaine de caractères : ")
CH1=CH[0]
nb=0
#boucle for(pour); comparer les premier lettres de chaque mot de CH
for i in range(0,len(CH)-1):
    if i==CH.find(" ")+1:
        if CH1.upper()==CH[i].upper():
            nb=1
        else:
            nb=0
#affichage
if nb==1:
    print("La chaine '",CH,"' est un tautogramme")
else:
    print("La chaine'",CH,"''n'est pas un tautogramme")