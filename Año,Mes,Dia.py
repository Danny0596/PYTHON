# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:41:54 2020

@author: Danny Lema
"""

def daysInMonth(day,month,years): 
    if years % 400 == 0:
        return True
    elif years % 100 == 0:
        return False
    elif years % 4 == 0:
        return True
    else:
        return False
year = 1900
print (year, daysInMonth(year))
year = 2000
print (year, daysInMonth(year))
year = 2016
print (year, daysInMonth(year))
year = 1987
print (year, daysInMonth(year))


