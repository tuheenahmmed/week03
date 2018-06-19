# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:03:50 2018

@author: etuhahm
"""
'''
hangman, final, submitted in grader
'''

def isWordGuessed(secretWord, lettersGuessed):

    compareword=str()

    for i in secretWord:
        for j in lettersGuessed:
                
            if  [j] == [i]:
                  compareword+=str(j)

                  break   

    return compareword ==secretWord



def getGuessedWord(secretWord, lettersGuessed):

    compareword=str()

    for i in secretWord:
        for j in lettersGuessed:
                
            if  [i] == [j]:
                compareword+=(j)
                break   
            
        else:
                
            compareword+='_ '

    return compareword




def getAvailableLetters(lettersGuessed):
 
    import string
    alphabet=list(string.ascii_lowercase)


    for i in lettersGuessed:
   
        for j in alphabet:
          
            if [i] == [j]:
            
                alphabet.remove(i)
           
                break
    return ''.join(alphabet)
        

def hangman(secretWord):

    
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


secretWord='C'
#secretWord = chooseWord(wordlist).lower()
hangman(secretWord)