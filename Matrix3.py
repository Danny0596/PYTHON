# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:11:24 2020

@author: Danny Lema
"""

import numpy as np
matrix=np.array([[1,2,3,4,5],[5,6,8,9,10]],dtype=np.int64)
print(matrix)
print("\n")
print("La matriz tiene:", matrix.ndim,"dimensiones")
print("\n")
print("El tipo de datos de la matriz es: ", matrix.dtype)
print("\n")
print("El tamaño de la matriz es:",matrix.size)
print("\n")
print("La forma de la matriz es:",matrix.shape)
