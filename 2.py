# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
fibinocci_list = []
fibinocci_even = []

def fibinocci(x):
    x = 0
    y = 0
    z = 0 
    while len(fibinocci_list) < 100 and x + y < 4000000: 
        if len(fibinocci_list) == 0:
            x += 1
            fibinocci_list.append(x)
            y = x + x 
            fibinocci_list.append(y)
        else: 
            z = x + y
            fibinocci_list.append(z)
            x = y 
            y = z 
        
fibinocci(0)

for number in fibinocci_list: 
    if number % 2 == 0:
        number = number
        fibinocci_even.append(number)
    else:
        number == 0 
        
print(sum(fibinocci_even))

print(fibinocci_even[0:10])
