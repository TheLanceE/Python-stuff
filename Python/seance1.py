from numpy import *
def saisie():
    global n
    n=int(input("donner la taille du matrice: "))
    while not(3<=n<=10):
        n=int(input("donner la taille du matrice: "))
def remplir(M,n):
    for i in range(n):
        for j in range(n):
            M[i][j]=int(input("M["+str(i)+"]["+str(j)+"]="))
            
def afficher(m,n):
    for i in range(n):
        maxi=M[i][0]
        for j in range(n):
            if maxi<M[i][j]:
                maxi=M[i][j]
        print("le maximum de ligne",i,"est",maxi)
def diagonale1(M,n):
    s=0
    for i in range(n):
        s=s+M[i][i]
    return s
def diagonale2(m,n):
    s=0
    for i in range(n):
        s=s+M[i][n-i-1]
    return s


##
saisie()
M=array([[int]*n]*n)
remplir(M,n)
afficher(M,n)
print("La somme de diagonale 1 est",diagonale1(M,n))
print("la somme de diagonale 2 est",diagonale2(M,n))