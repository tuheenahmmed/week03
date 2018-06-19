#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 05:44:16 2018

@author: tuheenahmmed
"""

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/etuhahm/Desktop/Python_guni/week03/problem_set_03/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()




def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    compareword=str()

    for i in secretWord:
        for j in lettersGuessed:
                
            if  [j] == [i]:
                  compareword+=str(j)

                  break   
 
#        print (len(compareword))
#        print (len(secretWord))
    return compareword ==secretWord

#print(isWordGuessed('apple', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']))




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...


    compareword=str()

    for i in secretWord:
        for j in lettersGuessed:
                
            if  [i] == [j]:
                compareword+=(j)
                break   
            
        else:
                
            compareword+='_ '

    return compareword

#print(getGuessedWord('apple', ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']))
#print(getGuessedWord('broccoli', [ ]))





def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
        
    import string
    alphabet=list(string.ascii_lowercase)


    for i in lettersGuessed:
   
        for j in alphabet:
          
            if [i] == [j]:
            
                alphabet.remove(i)
           
                break
    return ''.join(alphabet)
        
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    

    
    lettersGuessed =list()
    guess = secretWord
    guessInLowerCase = guess.lower()
    x= len(guessInLowerCase)


    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " +str(x)+ " letters long")
    print ("-------------")
    
    
    
    n=8
    while n !=0:
        

            print ("You have " + str(n)+" guesses left.")
            print ("Available letters: ", getAvailableLetters(lettersGuessed))
            guessLetter = input("Please guess a letter: ")
            
            

            if all ([guessLetter in guessInLowerCase , guessLetter not in lettersGuessed]):
                    
                    lettersGuessed+= guessLetter
                    print ("Good guess: ", getGuessedWord(guessInLowerCase, lettersGuessed))
                    print ("-------------")

                    n=n+1
                
         
                    if getGuessedWord(guessInLowerCase, lettersGuessed) == guessInLowerCase:
                    
                        print ("Congratulations, you won!") 
                        break
            
            elif guessLetter not in getAvailableLetters(lettersGuessed):
            
                print ("Oops! You've already guessed that letter: ",getGuessedWord(guessInLowerCase, lettersGuessed))
                print ("-------------")
                n = n+1
            
            else:
                lettersGuessed+= guessLetter
                print ("Oops! That letter is not in my word: ",getGuessedWord(guessInLowerCase, lettersGuessed))
                print ("-------------")
            n = n-1
            

            #lettersGuessed+= guessLetter
            
    else:
        print ("Sorry, you ran out of guesses. The word was "+str(guessInLowerCase)+str('.'))  




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
