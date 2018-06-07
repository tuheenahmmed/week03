#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 05:56:32 2018

@author: tuheenahmmed
"""

animals = {}

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']

animals['d'].append('dog')

animals['d'].append('dingo')

 

animals['e'] = ['pig']

animals['e'].append('dingo')


def biggest(animals):

    if animals == {}:

        return

    else: 

         biggest=0

         for i in animals:

             if len (animals[i]) > biggest:

                 biggest = len (animals[i])

         return i

            
print(biggest(animals))


###########second ###############
#################################


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']

animals['d'].append('dog')

animals['d'].append('dingo')

 

animals['e'] = ['pig']

animals['e'].append('dingo')


def biggest(animals):

    if animals == {}:

        return

    else: 

         biggest=0

         for i in animals:

             if len (animals[i]) > biggest:

                    biggest = len (animals[i])
                    x = i
                    print (biggest)
                    print (i)
    return x

            
print(biggest(animals))




''''
final and graded one
''''

aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

aDict['d'] = ['donkey']

aDict['d'].append('dog')

aDict['d'].append('dingo')

 

aDict['e'] = ['pig']

aDict['e'].append('dingo')


def biggest(aDict):

    if aDict == {}:

        return

    else: 

         biggest=0

         for i in aDict:

             if len (aDict[i]) > biggest:

                    biggest = len (aDict[i])
                    x = (i)
                    #print (biggest)
                    #print (i)
    return x

            
biggest(aDict)

print (biggest(aDict))






