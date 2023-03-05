#saisir
ch=input("Saisir la chaine : ")
i=0
j=len(ch)-1
test=True
#boculetantque
while (i<j) and (test==True):
    if ch[i]==ch[j]:
        i=i+1
        j=j-1
    else:
        test=False
#affichage
Msg="Palindrome"
if test==False:
    Msg="Non Palindrome"
print(ch,"est",Msg)
