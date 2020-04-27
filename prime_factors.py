#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:43:26 2020

@author: yash
this function calculates the factors of any number which are only prime numbers
it reduces the factors of a number to its prime factors

"""


import math
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print (2),
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print (i),
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print (n)
