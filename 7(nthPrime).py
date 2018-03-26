# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:39:54 2018

@author: mreich
"""
number = int(input("Find primes up to what number?: "))
prime_numbers = []


for x in range(2, number + 1): 
    isPrime = True 
    for y in range(2, int(x**.5)+1): 
        if x % y == 0:
            isPrime = False
            break
    if isPrime: 
        prime_numbers.append(x) 
            
print(max(prime_numbers))
print(len(prime_numbers))
print(prime_numbers[10000])