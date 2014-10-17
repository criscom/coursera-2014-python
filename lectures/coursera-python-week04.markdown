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



(Controlling position vs velocity) [https://d396qusza40orc.cloudfront.net/interactivepython/source_videos/week4-redo/velocity_control.pdf]