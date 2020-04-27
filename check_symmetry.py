#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:49:53 2020

@author: yash

# function to see if a list is symmetrical 
(Symmetrical here means the numbers of the list can be rearranged to be symmetrical): 
1. get the length of list
2. get the count of each element in the list
3. then if count of each element is even
4. if there is an element with odd count then the len of list must be odd


"""


def sym(lst):
    l = len(lst)
    s = set(lst)
    dic = {}
    for i in set(lst):
        dic[i] = lst.count(i)
    print(dic)
    if len(s)%2 == 0:
        print('symmetrical')
    else:
        v = 0
        for k in dic:
            v += dic.get(k)
        if v%2 == 0:
            print('non symmetrical')
        else:
            print('symmetrical')

sym([1,1,2,3,3])
