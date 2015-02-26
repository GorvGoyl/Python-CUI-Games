from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    
Function call: compChooseWord({'q': 1}, <edX internal wordList>, 1)
Output:
'None'
Function call: compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, <edX internal wordList>, 6)
Output:
'appels'
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    bword=''
    for xyz in wordList:
        if(isValidWord(xyz, hand, wordList)==True):
            if(getWordScore(xyz, n)>getWordScore(bword, n)):
                bword=xyz
    
    if(len(bword)>0):
        return bword
    else:
        return 'None'
    # Create a new variable to store the maximum score seen so far (initially 0)

    # Create a new variable to store the best word seen so far (initially None)  

    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    
Function call: compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, <edX internal wordList>, 6)
Test Case 1
Output:
current hand:  a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 110 points.
None
Function call: compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, <edX internal wordList>, 5)
Test Case 2
Output:
current hand:  a a c b t
"acta" earned 24 points. Total: 24 points
current hand:  b
Total score: 24 points.
None
    """
    # TO DO ... <-- Remove this comment when you code this function
    word=''
    count=0
    while(word!='None'):
        word=compChooseWord(hand, wordList, n)
        if(word!='None'):
            print "current hand: ",
            displayHand(hand)
            count+=getWordScore(word, n)
            print("\""+str(word)+"\" earned "+str(getWordScore(word,n))+" points. Total: "+str(count)+" points")
            hand=updateHand(hand,word)
            if calculateHandlen(hand)==0:
                break
        
    if calculateHandlen(hand)!=0:
        print "current hand: ",
        displayHand(hand)
    print("Total score: "+str(count)+" points.")
    
def compChooseWord(hand, wordList, n):
    bword=''
    for xyz in wordList:
        if(isValidWord(xyz, hand, wordList)==True):
            if(getWordScore(xyz, n)>getWordScore(bword, n)):
                bword=xyz
    
    if(len(bword)>0):
        return bword
    else:
        return 'None'
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)

Function call: playGame(<edX internal wordList>)
Test 3: Playing three user games, then quitting.
Output:
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Enter u for user to play, c to computer to play: u
Hand passed to playHand:  a z
<playHand execution not shown for grading brevity>
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Enter u for user to play, c to computer to play: u
Hand passed to playHand:  q i
<playHand execution not shown for grading brevity>
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Enter u for user to play, c to computer to play: u
Hand passed to playHand:  d o
<playHand execution not shown for grading brevity>
Enter n to deal a new hand, r to replay the last hand, or e to end game: e
None
    """
    # TO DO... <-- Remove this comment when you code this function
    new={}
    while True:
        u=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if u=='n':
            new=dealHand(HAND_SIZE)
            new1=new.copy()
            while True:
                v=raw_input('Enter u for user to play, c to computer to play: ')
                if v=='u':
                    playHand(new1,wordList,HAND_SIZE)
                    break
                elif v=='c':
                    compPlayHand(new1,wordList,HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        elif u=='r':
            if new=={}:
                print 'You have not played a hand yet. Please play a new hand first!'
                print
            else:
                new2=new.copy()
                while True:
                    v1=raw_input('Enter u for user to play, c to computer to play: ')
                    if v1=='u':
                        playHand(new2,wordList,HAND_SIZE)
                        break
                    elif v1=='c':
                        compPlayHand(new2,wordList,HAND_SIZE)
                        break
                    else:
                        print 'Invalid command.'
        elif u=='e':
            break
        else:
            print 'Invalid command.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


