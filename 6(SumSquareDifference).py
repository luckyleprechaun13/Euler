# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:21:18 2018

@author: mreich
"""
list_1 = []
list_2 = []

for a in range(1,101):
    x = a ** 2 
    list_1.append(x)

y = 0
for b in range(1,101):
    y += b   
    z = y ** 2  
    list_2.append(z)
    
        
print(max(list_2) - sum(list_1)) 