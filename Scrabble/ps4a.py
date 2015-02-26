# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    
Example:
getWordScore(was, 7)
Output:18
getWordScore(outgnaw, 7)
Output:127
    """
    # TO DO ... <-- Remove this comment when you code this function
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    sum=0
    for xv in word:
        sum=sum+SCRABBLE_LETTER_VALUES.get(xv,0)
    if len(word)==n:
        return (sum*len(word)+50)
    else:
        return (sum*len(word))



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
 Example:
 Function call: updateHand({'a': 1, 'i': 1, 'm': 1, 'l': 2, 'q': 1, 'u': 1}, quail)
Output: {'a': 0, 'q': 0, 'u': 0, 'i': 0, 'm': 1, 'l': 1}

Function call: updateHand({'g': 1, 'd': 1, 'o': 1}, dog)
Output: {'o': 0, 'd': 0, 'g': 0}
    """
    # TO DO ... <-- Remove this comment when you code this function
    dict=hand.copy()
    for x in word:
        if dict[x]>0:
            dict[x]=dict[x]-1
    return dict


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    
Example:
Function call: isValidWord(kwijibo, {'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 1}, <edX internal wordList>)
Output:False

Function call: isValidWord(hammer, {'a': 1, 'h': 1, 'r': 1, 'm': 2, 'e': 1}, <edX internal wordList>)
Output:True
    """
    # TO DO ... <-- Remove this comment when you code this function
    count=0
    worddict=getFrequencyDict(word)
    if word in wordList:
        for letter in worddict.keys():
            for j in hand.keys():
                if (letter==j) and worddict[letter]<=hand[j]:
                    count+=1
    if count==len(worddict) and word!='':
        return True
    else:
        return False

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer

Function call: calculateHandlen({'y': 0, 'x': 0, 'z': 0})
Output:0
Function call: calculateHandlen({'c': 1, 'i': 1, 'm': 3, 'l': 1, 'q': 2, 'u': 2, 'v': 1, 'x': 1, 'z': 2})
Output:14
    """
    # TO DO... <-- Remove this comment when you code this function
    count=0
    for letter in hand.keys():
        count+=hand[letter]
    return count


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

Function call: playHand({'k': 1, 'c': 1, 'u': 1, 'd': 1}, '<edX internal wordList>', 4)
Test 1: Using all the letters in the hand on the first guess
Output:
current hand:  k c u d
Enter word, or a "." to indicate that you are finished: duck
"duck" earned 94 points. Total: 94 points
Run out of letters. Total score: 94 points.
None
None

Function call: playHand({'y': 1, 'x': 2, 's': 1, 'z': 2, 'b': 1}, '<edX internal wordList>', 7)
Test 4: Can't make a word :(
Output:
current hand:  y x x s z z b
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 0 points.
None
None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    word=''
    count =0
    while(word!='.' and calculateHandlen(hand)!=0):
        print "current hand: ",
        displayHand(hand)
        word=(raw_input("Enter word, or a \".\" to indicate that you are finished: "))
        if(word=='.'):
            print("Goodbye! Total score: "+str(count)+" points.")
            break
        elif(isValidWord(word, hand, wordList)!=True):
            print "Invalid word, please try again."
        else:
            count+=getWordScore(word,n)
            print("\""+str(word)+"\" earned "+str(getWordScore(word,n))+" points. Total: "+str(count)+" points")
            hand=updateHand(hand,word)
        if calculateHandlen(hand)==0:
            print("Run out of letters. Total score: "+str(count)+" points.")        
            break
    print "None"
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    
Function call: playGame(<edX internal wordList>)
Test 1: Playing a single game, then quitting.
Output:
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Hand passed to playHand:  a c b
<playHand execution not shown for grading brevity>
Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
    
    """
    # TO DO ... <-- Remove this comment when you code this function
    c=0
    
    while(True):
        ch=(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        if (ch=='n'):
            c+=1
            rhand=dealHand(HAND_SIZE)
            playHand(rhand, wordList,HAND_SIZE)
        elif(ch=='e'):
            break
        elif(ch=='r'):
            if(c>0):
                playHand(rhand, wordList,HAND_SIZE)
            else:
                print"You have not played a hand yet. Please play a new hand first!"
        else:
            print"Invalid command."


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
