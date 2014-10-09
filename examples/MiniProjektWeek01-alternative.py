#############################################################################
# http://www.codeskulptor.org/#user38_4uyisU4UKe_0.py
# alternative program

# To Implement Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random
# helper functions

def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        return "Invalid Input!!!"

def number_to_name(number):
     if (number == 0):
        return "rock"
     elif (number == 1):
        return "Spock"
     elif (number == 2):
        return "paper"
     elif (number == 3):
        return "lizard"
     elif (number == 4):
        return "scissors"
     else:
        return "Invalid Input!!!"   

def rpsls(player_choice): 
    print
    print "Player chooses",player_choice
    a = name_to_number(player_choice)
    b = random.randint(0,4)
    print "Computer chooses",number_to_name(b)
    result = ((a-b)%5)
    if (result == 2) or (result == 1):
        print "Player wins!"
    elif (result == 0):
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    
# test codes
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")