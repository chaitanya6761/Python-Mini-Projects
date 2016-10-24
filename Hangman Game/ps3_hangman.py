# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/chaitanya/Downloads/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    flag=0
    for c in secretWord :
        if c not in lettersGuessed :
            flag+=1
    if flag >= 1 :
        return False
    else :
        return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess=''
    for c in secretWord :
        if c not in lettersGuessed :
            guess+='_ '
        else :
            guess += c
    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    listAlpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    str=''
    for c in listAlpha :
        if c not in lettersGuessed :
            str+=c
    return str
    

# When your hangman function passes the checks in the previous
# box, paste your function definition here to test it on harder 
# input cases.

def hangman(secretWord):
    
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+ str(len(secretWord)) +' letters long.'
    print '-------------'
    
    NumOfGuess=8
    lettersGuessed=[]
    temp=[]
    flag=0
    while NumOfGuess >= 1 :
        
        print 'You have '+str(NumOfGuess)+' guesses left.'
        print 'Available letters: ',getAvailableLetters(lettersGuessed)
        char=raw_input('Please guess a letter: ')
        lettersGuessed.append(char)
        if char in temp :
            print "Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed)
        elif char not in secretWord :
            print 'Oops! That letter is not in my word: ',getGuessedWord(secretWord, lettersGuessed)
            NumOfGuess-=1
        
        else :   
            print 'Good guess: ',getGuessedWord(secretWord, lettersGuessed)
        print '------------'    
        temp.append(char)
        
        if isWordGuessed(secretWord, lettersGuessed) :
            flag=1
            break

    if flag==1 :
        print 'Congratulations, you won!'
        
    else :    
        print 'Sorry, you ran out of guesses. The word was else.'










# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
