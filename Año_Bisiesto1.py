# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:41:54 2020

@author: Danny Lema
"""


def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
year = 1900
print (year, isYearLeap(year))
year = 2000
print (year, isYearLeap(year))
year = 2016
print (year, isYearLeap(year))
year = 1987
print (year, isYearLeap(year))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
