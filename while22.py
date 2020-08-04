# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:35:02 2020

@author: Danny Lema
"""


dato=int(input("Ingrese el numero a contar:" ))
contador=1
acumulador=0
while contador <=dato:
    print(contador,end=" ")
    acumulador+=contador
    contador+=1
print ("la suma de los # es:", acumulador)
print("El promedio total es: ", acumulador/dato)