from numpy import array
from random import *
def remplir(M):
    for i in range(4):
        for j in range(4):
            M[i][j]=randint(0,9)
def afficher(M):
    sb=0
    sn=0
    for i in range(4):
        for j in range(4):
            if i%2==0:
                if j%2==0:
                    sb=sb+M[i][j]
                else:
                    sn=sn+M[i][j]
            if i%2!=0:
                if j%2!=0:
                    sb=sb+M[i][j]
                else:
                    sn=sn+M[i][j]
    print('la somme de cases blanche est',sb)
    print('la somme de cases noirs est ',sn)
##
M=array([[0]*4]*4)
remplir(M)
print(M)
afficher(M)
