from numpy import array
"""
code modulaire
"""
#saisir;controleé
def saisie():
    N=int(input("Saisir le taille du matrice :"))
    while not(2<=N<=15):
        print("Unvalid! donnez un nombre entre 2 et 15")
        N=int(input("Saisir le taille du matrice :"))
    return N
#remplir;carre
def remplir(M,N):
    for i in range(N):
        for j in range(N):
            M[i,j]=input("M["+str(i)+","+str(j)+"]: ")
            while not("A"<=M[i,j]<="Z"):
                M[i,j]=input("M["+str(i)+","+str(j)+"]: ")
#verifpalin
def verif_palin(ch):
    a=0
    b=len(ch)-1
    ch=ch.upper()
    test=True
    while ((a<=b)and(test)):
        if ch[a]==ch[b]:
            a+=1
            b-=1
        else:
            test=False
    return test
#affich
def affich(M,N):
    for h in range(N):
        for k in range(N):
            print(M[h,k],end="|")
        print()
#affichpalin
def affich_palin(M,N):
    nbl=0
    nbc=0
    lg_ph=""
    col_ph=""
    for i in range(N):
        motlg=""
        motcol=""
        for j in range(N):
            motlg+=M[i,j]
            motcol+=M[j,i]
        if verif_palin(motlg):
            lg_ph+=motlg+"*"
            nbl+=1
        if verif_palin(motcol):
            col_ph+=motcol+"*"
            nbc+=1
    print(lg_ph[:len(lg_ph)-1])
    print(nbl)
    print(col_ph[:len(col_ph)-1])
    print(nbc)
"""
Code Principale
"""
N=saisie()
M=array([[str()]*N]*N)
remplir(M,N)
affich(M,N)
affich_palin(M,N)