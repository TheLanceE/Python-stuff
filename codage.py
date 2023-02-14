#saisir; controleé ,convertir les chaines en majuscules; PROCEDURE
def saisir():
    global ch
    ch=""
    while ch.find(".")== -1:
        ch=input("Donner une chaine qui se terminant avec un point : ")
        ch=ch.upper()
#crypt_saisir; saisir de p et q; controleé; PROCEDURE
def crypt_saisir():
    global p
    global q
    p=0
    q=0
    while not ((2=<p=<10)and(2=<q=<10)):
        p=int(input("Donner le premier entier : "))
        q=int(input("Donner le deuxieme entier : "))
#crypt; le cryptage; FONCTION
def crypt(x,y,c):
    for k in range(0,len(c)-1):