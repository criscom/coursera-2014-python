# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# importing modules

import simplegui
import random
import math

# initialize global variables

num_range = 100
# secret number for guess
secret_number = 0
# number of guesses
guesses = 0


# helper function to start and restart the game
def new_game():
    global secret_number
    # secret number for guess in the range of 0 - 100
    secret_number = random.randrange(0,101)
    print "New game. Range is from 0 to 100."
    print "Number of remaining guesses is 7."
    global guesses
    guesses = 7



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = range(0,1001)
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is 10."
    
def input_guess(guess):
        # main game logic goes here
    guess = int(guess)
    print "Your guess was:", guess
    global guesses
    guesses = guesses - 1
    print "Number of remaining guesses is", guesses
    
    

    
# create frame

# create simple gui frame

frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame

#create range button 100
frame.add_button('Range is (0, 100)', range100, 200)

#creae range button 1000
frame.add_button('Range is (0, 1000)', range1000, 200)

# create input field
frame.add_input('Make your guess', input_guess, 50)

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
