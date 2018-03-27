#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:03:08 2018

@author: MReich
"""
number = int(input("Find primes up to what number?: ")) #2000000
prime_numbers = []
for x in range(2, number + 1): 
    isPrime = True 
    for y in range(2, int(x**.5)+1): 
        if x % y == 0:
            isPrime = False
            break
    if isPrime: 
        prime_numbers.append(x) 
        

print(sum(prime_numbers))       
