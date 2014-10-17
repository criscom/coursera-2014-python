#Week 4
## Lists

= Sequence type  

a punch of items to put in order/sequence  
list ==> []  
[] empty list  
[1,2,3] list of numbers  
['hello', 'goodbye'] a list of strings  
position = [4,9] // x, y; position/coordinates; variable and list

>list is a way of asscociating data



```python

# Create 

mt_list = []
print mt_list, "you can have a list without any elements"

l = [1, 3, 4 , -7, 43]
print l

l2 = ['milk', 'eggs', 'bread']
print l2

l3 = [[3, 4], ['a', 'b', 'c'], []]
print l3

# Access

print len(mt_list), len(l), len(13)
prtin length of list
# what applies to strings, also applies to lists
# list and strings are sequences

print "first element:", l[0]
print "last element", l[-1]

print l3[1]

l4 = l2 [1:3]
# starting at element up to but not including element 3
print l4

# Update

l2[0] = 'cheese'
print l2
```

*Keep lists consistent regarding types of elements: if you have strings in a list keep only strings in the list; if you have integers in a list, keep only integers in a list. Don't mix types!*

>The length of the list is the number of items in the list. Note that each item can itself be a list (with 0 or more elements of its own). Also, notice that some of the answer lists in this question have different types of elements. While this is legal in Python, you should avoid doing this.

_List are a collection of objects. They allow us to keep datata that belongs together together without of having a punch of variables to hold it_

##Keyboard input

```pyhton
# Keyboard echo

import simplegui

# initialize state
current_key = ' '

# event handlers
def keydown(key):
    global current_key
    current_key = chr(key)
    
def keyup(key):
    global current_key
    current_key = ' '
    
def draw(c):
    # NOTE draw_text now throws an error on some non-printable characters
    # Since keydown event key codes do not all map directly to
    # the printable character via ord(), this example now restricts
    # keys to alphanumerics
    
    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        c.draw_text(current_key, [10, 25], 20, "Red")    
        
# create frame             
f = simplegui.create_frame("Echo", 35, 35)

# register event handlers
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.set_draw_handler(draw)

# start frame
f.start()
```

```python
# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
```

##Motion

velocity: 25 mbh  
time: 0

position = velocity * time  
if velocity is constant

```python
# Ball motion with an explicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 3]  # pixels per tick
time = 0

# define event handlers
def tick():
    global time
    time = time + 1

def draw(canvas):
    # create a list to hold ball position
    ball_pos = [0, 0]

    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()
```

###Points & Vectors
####Point
position = [3,4]

####Vector
I can take a vector and add it to a point. 

####Calculus
position(t) // position is a function of time
velocity(t)

_==> p(t+1) = p(t) + (1)*(v(t))_  
oder  
p(t+1) = p(0) + (t+1) + (v)

>The primary operation we will use on vectors and points is to add a vector to a point to get a new point. This is how we will move objects on the canvas from one point to another. Note that if you can add a vector to a point to get another point, then if you subtract two points, you should get a vector. You should never add two points together, this results in a meaningless value.

```python
# Ball motion with an implicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 1] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
```

##Collisions and reflections

####Two points
*Math - points on canvas*  
`p,q`

*Python - list of coordinates*  
`[p[0], p[1]], [q[0], q[1]]`

_Pythagorean theorem_  
*Math*  
`dist(p,q)**2 == (p[0] - q[0])**2 + (p[1] - q[1])**2`

*Python*
```python
def dist(p,q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
``` 

###Vector as difference of two points

*Math*  
`v = p - q`

*Python - list of components*  
`v[0] = p[0] - q[0]`  
`v[1] = p[1] - p[1]`

####Move/translate point using a vector

*Math*  
`p = q + v`

*Python*  
`p[0] = q[0] + v[0] # horizontal position`  
`p[1] = q[1] + v[1] # vertical position`

####Update for motion

*Math*  
The new position of an object is the old position plus a constant a times velocity  
`p = p + a * v`

*Python*  
`p[0] = p[0] + a * v[0]`
`p[1] = p[1] + a * v[1]`

###Collisions

####Collision of point p with wall

*Left wall*  
`p[0] <=0`

*Right wall*  
`p[0] >= width-1`

*Collision of ball of width center p and radius r with wall*

*Left wall*  
`p[0]<=r`

*Right wall*  
`p[0]>= (width - 1) - r`

![Collision of ball of width center p and radius r with wall](https://www.evernote.com/shard/s272/sh/dbc9c637-cb56-47dd-b85d-ed0845c7a02a/c2a6d48aa9907b34f2d62767bba6bc92/res/604b3ca0-e588-4a17-bdee-deda38902bbc/skitch.png)


###Reflections - update the velocity vector v

*Left wall*  
*Compute reflected velocity vector*  
`v[0] = -v[0]`  
`v[1] = v[1]`

![compute reflected velocity vector](https://www.evernote.com/shard/s272/sh/db6f8f1b-fdba-42d0-bd7d-e84634ccc99a/05b427b30349468331589886babef728/res/1a58d536-b103-4e8a-b455-295b4562703c/skitch.png)

```python
import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
```

###Bouncing on all four walls
>my own version

```python
import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-100.0 / 60.0,  50.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]

    # collide and reflect off of right hand side of canvas
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
         vel[0] = - vel[0]
    
    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        vel[1] = - vel[1]
    
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = - vel[1]
    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
```

##Velocitiy Control

```python
# control the velocity of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    acc = 1
    if key==simplegui.KEY_MAP["left"]:
        vel[0] -= acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0] += acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] -= acc
        
    print ball_pos
    
# create frame 
frame = simplegui.create_frame("Velocity ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
```

>Hold down key increment component of velocity vector; when you release key you decrement component of the vector

[! Controlling position vs velocity](https://www.evernote.com/shard/s272/sh/bdb02a6a-9ff1-47f9-89a7-8b71a70b2e36/ad141802566d4cec896db670810e0a8a/res/72be6ec7-44cf-4fda-932c-db55bcadcbe0/skitch.png)
[Controlling position vs velocity] (https://d396qusza40orc.cloudfront.net/interactivepython/source_videos/week4-redo/velocity_control.pdf)

##Visualizing lists and mutations

```pyhton
###################################
# Mutation vs. assignment


################
# Look alike, but different

a = [4, 5, 6]
b = [4, 5, 6]
print "Original a and b:", a, b
print "Are they same thing?", a is b

a[1] = 20
print "New a and b:", a, b
print

################
# Aliased

c = [4, 5, 6]
d = c
print "Original c and d:", c, d
print "Are they same thing?", c is d

c[1] = 20
print "New c and d:", c, d
print

################
# Copied

e = [4, 5, 6]
f = list(e)
print "Original e and f:", e, f
print "Are they same thing?", e is f

e[1] = 20
print "New e and f:", e, f
print


###################################
# Interaction with globals


a = [4, 5, 6]

def mutate_part(x):
    a[1] = x

def assign_whole(x):
    a = x

def assign_whole_global(x):
    global a
    a = x

mutate_part(100)
print a

assign_whole(200)
print a

assign_whole_global(300)
print a
```
> When doing mutations like `a[1] = x` in a function, the variable `a` is considered to be _global_ automatically without defining `a` as `global`.

##Mutability

use the _is_ keyword to find out what is mutable.

`print 1 is 1` is `True`
`print 1.0 is 1.0` is `True`
`print [4, 5, 6] is [4, 5, 6]` is `False`
`print (4, 5, 6) is (4, 5, 6)` is `False` ==> Tuple


###Tuples

>They act like lists but they are not mutable.

_Remember that strings like tuples are immutable._

```python
###################################
# Lists (mutable) vs. tuples (immutable)

print [4, 5, 6]

print (4, 5, 6)

print type([4, 5, 6])

print type((4, 5, 6))

a = [4, 5, 6]
a[1] = 100
print a

b = (4, 5, 6)
b[1] = 100
print b
```

![Tuple example](https://www.evernote.com/shard/s272/sh/2fc5f0ae-44e9-4de8-a69d-6f738252d8bb/533980398897f1d1551cdd99b0933b31/res/a2016d77-5c7a-4471-a0e6-4bddaa5907bb/skitch.png)

##Pong
![Pong](https://www.evernote.com/shard/s272/sh/aa052b34-1379-4572-ba9b-a58e6398fe56/f2cb868e091d60463f2dba0e3b2f0547/res/ebb65643-835f-4b17-b62b-89dfcbe8152b/skitch.png)   
![Pong geometry](https://www.evernote.com/shard/s272/sh/0665dd42-ad0b-4890-b612-2d3647a9e1ca/bad7258da3785a0b51b342ec108de26b/res/d736a7e1-3fd3-4bb6-aa89-fab7372361f5/skitch.png)

###Program template for Pong game

```python
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
            
    # draw ball
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()

```