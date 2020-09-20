#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:48:49 2020

@author: lingg
"""
#Q1 O(n ^2)
#isSubset(['A','B','C','D','E'], ['A','E','D'])
#isSubset(['A','B','C','D','E'], ['A','E','D'])
#isSubset(['A','B','C','D','E'], ['A','D','Z'])
def isSubset(arrayA, arrayB):
    mark = len(arrayB) #check size of arrayB
    check = 0
    for x in arrayB: #go thriugh each element of arrayB (O(n ^2))
        for y in arrayA: #go thriugh each element of arrayA (O(n ^2))
            if y != x:continue #check that x is not equal to y, return to the second loop
            else:
                check += 1 #check that x is a element of arrayA, maek it
                break #stop the second loop to reduce the looping time
    if check == mark : return True
    else: return False
    