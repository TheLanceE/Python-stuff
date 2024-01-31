from numpy import array
from math import randint

def saisir():
    n=int(input("Donner le taille du matrice: "))
    while not(3<n<8):
        n=int(input("Donner le taille du matrice: "))
def remplir(n):
    for i in range(n):
        for j in range(n):
            m[i][j]=randint(1,n*n)
def randppcm():