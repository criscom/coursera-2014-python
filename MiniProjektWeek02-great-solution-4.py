# "Guess the number" mini-project
# Created at: Oct.1th.2014
# Creator: Cope Cheung

import simplegui
import random
import math

secret_number = 0
low = 0
high = 100
remaining_number = 0

def new_game():
    global secret_number, remain_guess
    secret_number = random.randrange(low, high)
    remain_guess = int(math.ceil(math.log(high - low + 1,2)))
    print "\nThe new game starts! Please guess a number", "range=[0,", str(high) + ")","\nYou can also click on one of the two buttons to alter the range."


# define event handlers for control panel
def range100():
    global low, high
    low = 0
    high = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global low, high
    low = 0
    high = 1000
    new_game()

def input_guess(guess):
    global remain_guess
    remain_guess -= 1
    guess = int(guess)
    print "\nYour guess was", guess
    print "number of your remaining guesses is", remain_guess
    if secret_number > guess:
        print "Higher"
    elif secret_number < guess:
        print "Lower\n"
    else:
        print "\nCorrect!You win the game!"
        new_game()
        

    

f = simplegui.create_frame("Guess the number", 300, 300)

f.add_button("Range: 0 - 100", range100, 200)
f.add_button("Range: 0 - 1000", range1000, 200)
f.add_input("input_guess", input_guess, 100)

# call new_game 
f.start
new_game()
# always remember to check your completed program against the grading rubric

