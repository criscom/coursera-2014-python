#Week 3
## Canvas and drawing

Computer monitor - 2D grid pixels stored in frame buffer  
Computers update the monitor based on the frame buffer at rate of around 60-72 times a second - refresh rate  
Many applications will register a special function called a "draw handler".

In CodeScupltor, register the draw handler using a simpleGUI command. CodeSkulptor calls teh draw handler at around 60 times per seconds.

Draw handler updates the canvas using a collection of draw commands that include draw_text, draw_line, draw_circle

###Canvas coordinates

![alt text](https://www.evernote.com/shard/s272/sh/e645f62c-83db-41c8-9585-50a6487debd1/253f965b9ce146bb3e4f1997e4f29696/res/d64cd7f8-f88b-40f4-a094-38a54f3c2ce6/skitch.png)

[x,y] ==> origin is upper left  
x == width  
y == height  

```
# first example of drawing on the canvas

import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()
```

## String processing

```
### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[3]
print len(s1)
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38
```

*Get the first character out of a string*   
`print s1[0]`

*Get the last character out of a string*   
`print s1[-1]`

*Print the length of a string*   
`print len(s1)`

*Pull out a slice of a string*   
`print s1[0:7]`   
> Go from first character to 7th but don't include 7th

*Start at the 6th character and go to the end*   
`s2[6:]`

*Start at the beginning up to but not including 13*   
`s2[:13]`

*String indices begin at 0. String slices start from the first index and go up to, but not including, the last index.*

*Convert integer into a string with the str-function*  
`s5 = str(375)`

*Convet string into an integer with int function*  
`i1 = int(s5[1:])`

```
# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
    
# Tests
print convert(11.23)
print convert(11.20) 
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
```

##Interactive drawing

```
# interactive application to convert a float in dollars and cents

import simplegui

# define global value

value = 3.12

# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    

# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [60, 110], 24, "White")


# define an input field handler
def input_handler(text):
    global value
    value = float(text)


# create frame
frame = simplegui.create_frame("Converter", 400, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter value", input_handler, 100)


# start frame
frame.start()
```
*The canvas should always be drawn exclusively by the draw handler. No other code should try to update the canvas in any way.*

##Timers

```
# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text
    
# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
timer.start()
```

##Visualizing drawing and timers


