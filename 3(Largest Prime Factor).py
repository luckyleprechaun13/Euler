#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:44:45 2018

@author: MReich
"""

n = 500008
i = 2
while i < n:
     while n % i == 0:
         n = n / i
         print(n,i)
     i += 1

print(n) 

'''
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(600851475143))
'''
