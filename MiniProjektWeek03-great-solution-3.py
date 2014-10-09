# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

secret_number = 0
counter = 0
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    print "****************************"
    print "Play a guessing number game."
    print "****************************"
    if num_range == 100:
        range100()
    else:
        range1000()
        

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "Guess between 0 to 100. You have 7 guesses"
    print ""
    global secret_number
    global counter
    global num_range
    secret_number = random.randrange(0,100)
    counter = 7
    num_range = 100
 
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "Guess between 0 to 1000. You have 10 guesses"
    print ""
    global secret_number
    global counter
    global num_range
    secret_number = random.randrange(0,1000)
    counter = 10
    num_range = 1000
 
    
def input_guess(guess):
    # main game logic goes here 
    # Initialize gloabl variables
    global secret_number
    global counter
   
    print "Guess was %d" %int(guess)
    if int(guess) > secret_number:
        print "Guess Lower."
    elif int(guess) < secret_number:
        print "Guess Higher."
    else:
        print "Awesome!! Well Done."
        print ""
        new_game()
        guess = None
    
    # counter to check for maximum guesses
    counter -= 1
    if counter == 0:
        print "Oops!!!Maximum number of guesses reached"
        print""
        new_game()
    else:
        if guess == None:
            print ""
            counter += 1
        else:     
            print "You still have %d guesses" %counter
            print ""

# create frame
frame = simplegui.create_frame("input_guess",300,300)
label = frame.add_button('Range 0-100', range100, 200)
label = frame.add_button('Range 0-1000', range1000, 200)
inp = frame.add_input('Guess a number', input_guess, 50)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()



# always remember to check your completed program against the grading rubric

