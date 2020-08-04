# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:32:07 2020

@author: Danny Lema
"""


#valores con matriz aleatorio(random)
import numpy as np
matrix=np.array([[1,2,3,4,5],[5,6,8,9,10]],dtype=np.int64)
print(matrix)
unos=np.ones((5,4))
print(unos)
ceros=np.zeros((5,5))
print(ceros)
ran=np.random.random((4,4))
print(ran)
print("\n"*2)
ept=np.empty((5,5))
print(ept)