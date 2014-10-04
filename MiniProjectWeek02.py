# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# importing modules

import simplegui
import random
import math

# initialize global variables

# secret number to guess
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
    print ""
    #define the number of guesses
    global guesses
    guesses = 7



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    # we simply call new_game() function
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = range(0,1001)
    print "New game. Range is from 0 to 1000."
    print "Number of remaining guesses is 10."
    print ""
    #define the number of guesses
    global guesses
    guesses = 10
    
def input_guess(guess):
    # main game logic goes here
    #converting guess from a string to an integer
    guess = int(guess)
    #print the guess
    print "Your guess was:", guess
    #number of guesses, decremented with each guess
    global guesses
    guesses = guesses - 1
    print "Number of remaining guesses is", guesses
    
    #comparing guess with secret number
    
    #if guess is correct then start a new game
    if guess == secret_number:
        print "Correct! You are a champ!"
        print "Let's start a new game!"
        print ""
        #start a new game
        new_game()
        
    #if run out of guesses then start a new game
    #if guess is wrong and remaining guesses = 0
    elif guess != secret_number and guesses == 0:
        print "Wrong guess!"
        print "You have run out of guesses!"
        print "Let's start a new game!"
        print ""
        #start a new game
        new_game()
        
    elif guess > secret_number:
        print "Secret number is lower!"
        print ""
        
    elif guess < secret_number:
        print "Secret number is higher!"
        print ""
        
    
    

    
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
