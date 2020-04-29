#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:45:21 2020

@author: yash

The below code is to reverse a sentence

"""

def reverse(s):
    l = len(s)
    i = 0
    space = [' ']
    w = []
    while i < l:
        if s[i] not in space:
            word_start = i

            while i < l and s[i] not in space:
                i += 1
            w.append(s[word_start:i])
        i+=1


    return " ".join(s.split()[::-1])


# reverse a string
start = "this is the best"
finish = "best the is this"


reverse(start)



