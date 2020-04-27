#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:04:31 2020

@author: yash

This script contains functions to find if a word is a Palindrome or an Anagram

"""

# To Check if the word is a Palindrome
def palin(word):
    a = word[::-1]
    if a == word:
        print('its a palindrome')
    else:
        print('not a palindrome')

palin('dod')



# To Check if the word is an Anagram 
def anagram(a,b):
    if sorted(a) == sorted(b):
        print('anagram')
    else:
        print('non anagram')
