# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

range_highvalue = 100
range_lowvalue = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, range_highvalue, range_lowvalue, num_playerguesses, num_maxguesses
    num_playerguesses = 0
    num_maxguesses = math.ceil(math.log(range_highvalue - range_lowvalue + 1,2))
    secret_number = random.randrange(range_lowvalue, range_highvalue) 
    # print actions
    print ""
    print "------------------------------------"
    print "New game, number of allowed guesses is",int(num_maxguesses)
    print "Choice out of",range_highvalue,"successive numbers (included",range_lowvalue,", excluded",range_highvalue,")"
    # print "secret number is:",secret_number  

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_highvalue
    range_highvalue = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_highvalue
    range_highvalue = 1000
    new_game()
       
def input_guess(guess):
    # used variables
    global range_highvalue, secret_number, num_playerguesses, num_maxguesses
    guessed_number = int(guess)
    succes = False
            
    # main game logic goes here 
    # preparing actions
    print ""
    print "Guess was:",guessed_number
    num_playerguesses = num_playerguesses + 1
    num_guessesremain = num_maxguesses - num_playerguesses
    
    # matching the numbers    
    if guessed_number < 0 or guessed_number >= range_highvalue:
        print "Warning: guessed number outside range(",range_lowvalue,",",range_highvalue,") also excluded",range_highvalue       
    elif guessed_number < secret_number:    
        print "Higher!"        
    elif guessed_number > secret_number:
        print "Lower!"
    else:
        succes = True
        print "Correct!"
        new_game()
        
    # determing the follow-up
    if not succes and num_guessesremain > 0:
        print int(num_guessesremain),"guesses left!"
    elif not succes and num_guessesremain == 0:
        print "no guesses left"
        new_game()
       
# create frame
frame_numguess = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
numguess_input = frame_numguess.add_input("Enter your guess", input_guess, 100)
range100_button = frame_numguess.add_button("Range is (0, 100)",range100, 200) 
range1000_button = frame_numguess.add_button("Range is (0, 1000)",range1000, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

