# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:11:08 2020

@author: Danny Lema
"""

 
#finaliza al ingresar "q" o "quit", utilizamos break

while True:
    x=input("ingrese el # de veces a contar:..")
    if x== "q" or x== "quit":
        break
    else:
        x=int(x)
        y=1
        while True:
            print (y)
            y= y+1
            if y>x:
                break
            