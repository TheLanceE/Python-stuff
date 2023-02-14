# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:21:19 2022

@author: Lance
"""

from numpy import*
def saisir():
    n=0
    while not (5<=n<=10):
         n=int(input("donner n"))
    return n
#########
def remplir(t,n):
    for i in range (n):
        t[i]=input("donner votre mot")
#########
def remplir2(x,n,t):
    for i in range(n):
           x[i]=voyelle(t[i])
#########
def voyelle(ch):
    nb=0
    for k in range(len(ch)):
        if (ch[k].upper()) in ["A","Y","O","U","I","E"]:
            nb=nb+1
        return nb
#########
def tri(t,x,n):
    test=False
    while test==False:
        test=True
        for i in range(n):
            if x[i]>x[i+1]:
                aux=x[i+1]
                x[i+1]=x[i]
                x[i]=aux
                t[i],t[i+1]=t[i+1],t[i]
                test=False
##########
def affichet(t,n):
    for i in range(n):
        print(t[i],end="|")
##########
def affichex(x,n):
    for l in range(n):
        print(t[l],end="|")
##pgpp##
n=saisir()
t=array([str]*n)
x=array([str]*n)
remplir(t,n)
remplir2(x,n,t)
nb=voyelle(t)
test=tri(t,x,n)