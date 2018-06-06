# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:56:53 2018

@author: etuhahm
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
#Assume that
testList = [1, -4, 8, -9]



        
'''
Exercise: apply to each 1
'''
applyToEach(testList, abs)     


############
'''
#Exercise: apply to each 2
'''

# Your Code Here
def addOne(a):
    return a+1

applyToEach(testList, addOne)

#############
'''
#Exercise: apply to each 3
'''

# Your Code Here
def MultiplySame(a):
    return a*a

applyToEach(testList, MultiplySame)





