# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict

Test 1: buildCoder(6)
Output:
{'A': 'G', 'C': 'I', 'B': 'H', 'E': 'K', 'D': 'J', 'G': 'M', 'F': 'L', 'I': 'O', 'H': 'N', 'K': 'Q', 'J': 'P', 'M': 'S', 'L': 'R', 'O': 'U', 'N': 'T', 'Q': 'W', 'P': 'V', 'S': 'Y', 'R': 'X', 'U': 'A', 'T': 'Z', 'W': 'C', 'V': 'B', 'Y': 'E', 'X': 'D', 'Z': 'F', 'a': 'g', 'c': 'i', 'b': 'h', 'e': 'k', 'd': 'j', 'g': 'm', 'f': 'l', 'i': 'o', 'h': 'n', 'k': 'q', 'j': 'p', 'm': 's', 'l': 'r', 'o': 'u', 'n': 't', 'q': 'w', 'p': 'v', 's': 'y', 'r': 'x', 'u': 'a', 't': 'z', 'w': 'c', 'v': 'b', 'y': 'e', 'x': 'd', 'z': 'f'}
    """
    ### TODO.
    d={}
    l=string.ascii_lowercase
    u=string.ascii_uppercase
    for i in range(len(u)):
        d[u[i]]=u[(i+shift)%26]
    for j in range(len(u),len(u)+len(l)):
        d[l[j%26]]=l[(j+shift)%26]
    return d

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    
Test 1: applyCoder('Hello, world!', buildCoder(2))
Output:
'Jgnnq, yqtnf!'
Test 2: applyCoder('Hello, world!', buildCoder(0))
Output:
'Hello, world!'
    """
    ### TODO.
    res=''
    for l in text:
        if l in coder.keys():
            res+=coder[l]
        else:
            res+=l
    return res
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    
Test 1: applyShift('Hello, world!', 17)
Output:
'Yvccf, nficu!'
Test 2: applyShift('The quiz is... hard!', 7)
Output:
'Aol xbpg pz... ohyk!'
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    coder=buildCoder(shift)
    return applyCoder(text,coder)
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
Test 1: findBestShift(<edX wordList>, 'Ifmmp, xpSme!')
Output:
25
Test 2: findBestShift(<edX wordList>, 'Ftq cgul ue... tmdp!')
Output:
14
    """
    ### TODO
    max_real=0
    bshift=0
    for i in range(26):
        test=applyShift(text,i).split()
        count=0
        for e in test:
            if isWord(wordList,e):
                count+=1
        if count>max_real:
            max_real=count
            bshift=i    
    return bshift
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
Test 1: decryptStory: ('Efejvejv nfiuj: xzic grcv ils dvdsvi jvrjfe')
Output:
'Nonsense words: girl pale rub member season'
Test 2: decryptStory: ('Opotfotf xpset: hjsm qbmf svc nfncfs tfbtpo')
Output:
'Nonsense words: girl pale rub member season'
    """
    ### TODO.
    i=findBestShift(loadWords(),getStoryString())
    return applyShift(getStoryString(),i)
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
	decryptStory()
