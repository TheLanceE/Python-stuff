#saisir; controleé
def saisir() :
    global ch
    ch=""
    while not(len(ch)>0):
        ch=input("Donner une chaine (non vide): ")
#affich_lettre; ASCII
def affich_lettre(L):
    LL=""
    for i in range(len(L)):
        if (ord(L[i])in range(97,123))or(ord(L[i])in range(65,91)):
            LL=LL+L[i]
    return (LL)
#affich_chiffre; liste (0...9)
def affich_chiffre(C):
    CC=""
    for i in range(len(C)):
        if (C[i]in ["0","1","2","3","4","5","6","7","8","9"]):
            CC=CC+C[i]
    return (CC)
#affich_symbole; ASCII
def affich_symbole(S):
    SS=""
    for i in range(len(S)):
        if (ord(S[i])in range(0,48))or(ord(S[i])in range(85,65))or(ord(S[i])in range(91,97))or(ord(S[i])in range(124,256)):
            SS=SS+S[i]
    return (SS)
#Programme Principale
saisir()
L_ch=affich_lettre(ch)
C_ch=affich_chiffre(ch)
S_ch=affich_symbole(ch)
print("La chaine des lettres est : ",L_ch ,"\nLa chaine des chiffres est : ",C_ch,"\nLa chaine des symboles est : ",S_ch)