# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:38:20 2020

@author: Danny Lema
"""


def dirección(calle,sector,codigopostal,referencia,numcasa):
    print("Su dirección es;","Su sector es:",sector,"calle:",calle)
    print("su casa es la numero:",numcasa,"Con cógido postal numero:", codigopostal)
    print("y esta cerda:", referencia)
    
print("Ingrese los datos solicitados: ")
c=input("ingrese la calle: ")
s=input("Ingrese sector de residencia: ")
cod=input("Ingrese # de casa: ")
r=input("Ingrese una referencia de su domicilio: ")
num=("Ingrese el # de casa: ")

dirección(c,s,cod,r,num)