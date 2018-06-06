# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:54:41 2018

@author: etuhahm
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many (animals):
    my_ani=0
    for i in animals:
      my_ani+= len (animals[i])
      #return my_ani
    return my_ani
  
print(how_many(animals))
    


len (animals['d'])

len (animals['d'])+ len (animals['a'])+ len (animals['b']) + len (animals['c'])

    

######final and graded one#############


aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

aDict['d'] = ['donkey']
aDict['d'].append('dog')
aDict['d'].append('dingo')



def how_many (aDict):
    my_ani=0
    for i in aDict:
      my_ani+= len (aDict[i])

    return my_ani
  
print(how_many(aDict))








    
    







