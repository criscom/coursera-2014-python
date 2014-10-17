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
TIME = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 10] # pixels per update (1/60 seconds)

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
 
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    

    
    # let ball bounce from top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        #top
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        #bottom
        ball_vel[1] = - ball_vel[1]
    
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "#669fb2")
                       
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    
# register event handlers


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('#cdf69f')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()