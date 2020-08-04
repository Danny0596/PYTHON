# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:58:58 2020

@author: Danny Lema
"""

x=int(input("ingrese el numero a contar:. "))
contador=1
acumulador=0
while True:
    print (contador)
    acumulador+=contador
    contador+=1
    if contador>x:
        break
print("la suma de los numeros es: ", acumulador)
print("El promedio de la suma es:.", acumulador/x)