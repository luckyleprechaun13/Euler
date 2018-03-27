# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:56:02 2018

@author: mreich
"""
'''
for a in range(1,1000):
    for b in range(a+1, 1000): 
        for c in range(b+1,1001):
            if c ** 2 == a ** 2 + b ** 2 and a + b + c == 1000:
                print(a*b*c)
'''

'''N = int(input("Enter the maximum 'Z' value: "))

for x in range(1,N):
    y = x+1
    z = y+1
    while z <= N:
        while z * z < x * x + y * y:
            z = z + 1
        if z * z == x * x + y * y and z <= N:
            print(x,y,z)
'''

for c in range(3,1000):
	for b in range (2,c):
		for a in range(1,b):
			if (a ** 2 + b **2 == c ** 2 and a + b + c == 1000):
				print (str(a * b * c))
				break