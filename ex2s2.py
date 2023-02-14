# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 09:49:42 2022

@author: Lance
"""

for i in range (1,51):
    if (i%3)==0:
        i="Fizz"
        print(i)
    elif (i%5)==0:
        i="Buzz"
        print(i)
    else:
        print(i)