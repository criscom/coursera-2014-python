#Coursera: Week 1#

##Functions##

**Always comment a function!**

def triangle_area(base, height): /* header ==> tells you about the function; a colon means you start a new block of code */  
    area = (1.0 / 2) * base * height // indention is important  
    return area // output of function

> a function only executes when you call it

a1 = triangle_area(3, 8)  
print a1 // prints the return value

####_converts fahrenheit to celsius_

def fahrenheit2celsius(fahrenheit):  
    celsius = (5.0 / 9) * (fahrenheit - 32)  
    return celsius  

_test_
c1 = fahrenheit2celsius(32)  
c1 = fahrenheit2celsius(212)  
print c1, c2

####_converts fahrenheit to kelvin_
_using a function inside a function_

def fahrenheit2kelvin(fahrenheit):  
    celsius = fahrenheit2celsius(fahrenheit)  
    kelvin = celsius + 273.15  
    return = kelvin  

####_prints hello, world!_

def hello():  
    print "Hello, world!"  

_test_  
hello()

> doesn't have a return value;
> if you forget return value, Python automatically adds a return value automatically. So if you see a "None" value in the output, you forgot the return value.

##Operations##

_Remainder - modular arithmetic_

_systematically restrict computation to a range_
_long division - divide by a number, we get a quotient plus a remainder_
_quotient is integer division //, the remainder is % (Docs)_


####_problem - get the ones digit of a number_
num = 49  
tens = num // 10  
ones = num % 10  
print tens, ones  
print 10 * tens + ones, num


**The "%" operator** computes the remainder of one number with respect to another**


####_application - 24 hour clock_
_http://en.wikipedia.org/wiki/24-hour_clock_

hour = 20  
shift = 8  
print (hour + shift) % 24  

####_Data conversion operations_

_convert an integer into string - str_
_convert an hour into 24-hour format "03:00", always print leading zero_

hour = 3  
ones = hour % 10  
tens = hour // 10  
print tens, ones, ":00"  
print str(tens), str(ones), ":00"  
print str(tens) + str(ones) + ":00"  


#####_Data conversion operations_

_convert an integer into string - str_  
_convert an hour into 24-hour format "03:00", always print leading zero_

hour = 3  
ones = hour % 10  
tens = hour // 10  
print tens, ones, ":00"  
print str(tens), str(ones), ":00"  
print str(tens) + str(ones) + ":00"

**_str_ converts integers into a string**
**the "+" operator joins strings together**

####_convert a string into numbers using int and float_



#####_Python modules - extra functions implemented outside basic Python_

import simplegui    _access to drawing operations for interactive applications_

import math         _access to standard math functions, e.g; trig_

import random       _functions to generate random numbers_

**random.randrange()** => have a look at it! will be used a lot!

_look in Docs for useful functions_

print math.pi

##Logic and conditionals##

def greet(friend, money):
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money


money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money
print ""

money = greet(True, money)
print "Money:", money
print ""



#### Conditionals Examples

##### Return True if year is a leap year, false otherwise
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False


year = 2012
leap_year = is_leap_year(year)
    
if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"



##Mini Project##

* 0 == rock
* 1 == Spock
* 2 == paper
* 3 == lizard
* 4 == scissors

[RPSLS clock](http://goo.gl/dc7zui)

###Rule
_beat counterclockwise oponents, lose clockwise opponents_

Spock always beats his counterclockwise opponents: rock, scissors  
Spoack always loses to his clockwise opponents: paper, lizard

Take the numbers for each of the items and look at their difference  
paper minus Spock  
2 - 1 = 1 therefore paper beats Spock

lizard vs Spock  
3 - 2 = 1 therefore lizard beats Spock

scissors vs Spock  
4 - 1 = 3

Spock vs scissors
1 - 4 = -3 % 5 ==> 2

rock vs Spock  
0 - 1 = - 1 % 5

**Use modular remainders**  
Remainder 5

If the difference is 1 or 2 the first item wins
If the difference is 3 or 4 the second item wins

###Instructions

1. Build function `rpsls(name)` with string inputs `"rock"`, `"paper"`, `"scissors"`, `"lizard"`, or `"Spock"

> The function then simulates playing a round of Rock-paper-scissors-lizard-Spock by generating its own random choice from these alternatives and then determining the winner using a simple rule that we will next describe.
