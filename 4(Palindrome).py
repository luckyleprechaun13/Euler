# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:24:28 2018

@author: mreich
"""

numbers = []
for x in range(1,1000):
    for y in range(1,1000):
        a = x*y
        if a > 100000:
            numbers.append(str(a))

palindromes = []      
for number in numbers:
    if str(number) == str(number)[::-1]:
        palindromes.append(number)

print(max(palindromes))