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

WORDLIST_FILENAME = "words.txt"

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
      
    implement the function isWordGuessed that
     takes in two parameters - a string, secretWord,
      and a list of letters, lettersGuessed.
       This function returns a boolean - True if secretWord
        has been guessed (ie, all the letters of secretWord
         are in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print isWordGuessed(secretWord, lettersGuessed)
False
    '''
    # FILL IN YOUR CODE HERE...
    flag=0
    for i in range(len(lettersGuessed)):
        for k in range(len(secretWord)):
            if lettersGuessed[i]==secretWord[k]:
                flag+=1
    if flag==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      
      implement the function getGuessedWord that takes 
      in two parameters - a string, secretWord, and a list of letters,
       lettersGuessed. This function returns a string that is
        comprised of letters and underscores, based on what 
        letters in lettersGuessed are in secretWord. This 
        shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getGuessedWord(secretWord, lettersGuessed)
'_ pp_ e'
    '''
    # FILL IN YOUR CODE HERE...
    res=''
    for letter in secretWord:
        if letter in lettersGuessed:
            res=res + letter
        else:
            res=res + ' _ '
    return res


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
      
      implement the function getAvailableLetters that takes
       in one parameter - a list of letters, lettersGuessed. 
       This function returns a string that is comprised of 
       lowercase English letters - all lowercase English letters 
       that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getAvailableLetters(lettersGuessed)
abcdfghjlmnoqtuvwxyz
    '''
    # FILL IN YOUR CODE HERE...
    res=''
    s='abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        if not letter in lettersGuessed:
            res=res+letter
    return res 

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
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long'
    print '-------------'
    i=8
    lettersGuessed=[]
    while i>0 and '_' in getGuessedWord(secretWord, lettersGuessed):
        print 'You have '+str(i)+' guesses left'
        print 'Available letters: '+ getAvailableLetters(lettersGuessed)
        guess=raw_input('Please guess a letter: ')
        guess=guess.lower()
        lettersGuessed.append(guess)
        if guess in secretWord:
            if lettersGuessed.count(guess)>1:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
        else:
            if lettersGuessed.count(guess)>1:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                i-=1
        print '------------'
    if isWordGuessed(secretWord, lettersGuessed):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was '+secretWord+'.'








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
