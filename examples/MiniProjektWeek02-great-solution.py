# "Guess the number" mini-project
 
# inmport the nedded libraries
import simplegui
import random

#as a defult the range will be [0,100) and as of that there is 7 guess
# Global variables declaration
wanted_range = 100
number_of_guess = 7
secret_number = 0

# helper function to start and restart the game
def new_game():
    global secret_number , wanted_range , number_of_guess
    
    if(wanted_range == 100):
        number_of_guess = 7
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is 7"
    else: # wanted_range == 1000
        number_of_guess = 10
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is 10"
    
    print "\n"        
    secret_number = random.randrange(0, wanted_range)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global wanted_range
    wanted_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global wanted_range 
    wanted_range = 1000
    new_game()
    
def input_guess(guess):
    global wanted_range , number_of_guess
    
    # the guess variable is of type string we need to convert it to intger 
    int_guess = int(guess)
         
    print "Guess was",int_guess
    
    number_of_guess = number_of_guess - 1
    
    print "Number of remaining guesses is",number_of_guess
    
    if(int_guess < secret_number):
        print "Higher!"
    elif(int_guess > secret_number):
        print "Lower!"
    else:
        print "Correct!"
        print "\n"
        new_game()
    
    print "\n"
    
    if(number_of_guess == 0):
        new_game()

    
# create frame
frame = simplegui.create_frame('Guess the number', 250, 250)

button1 = frame.add_button('Restart game', new_game)
button2 = frame.add_button('Range: 0 - 100', range100)
button3 = frame.add_button('Range: 0 - 1000', range1000)

inp_guess = frame.add_input('Yours guess goes here:', input_guess, 150)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()