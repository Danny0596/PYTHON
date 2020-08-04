# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:17:29 2020

@author: Danny Lema
"""
matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0]]
for i in range (0,5):
    for j in range(0,6):
        print("Ingrese el valor de la posicion:",i,j)
        matrix[i][j]=int(input())
print(matrix)
        