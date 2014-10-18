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
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2, 4] # pixels per update (1/60 seconds)
paddle1_pos = (HEIGHT / 2)
paddle1_vel = 0
paddle2_pos = (HEIGHT / 2)
paddle2_vel = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2,-4)
        ball_vel[1] = random.randrange(1,-3)
    if direction == LEFT:
        ball_vel[0] = random.randrange(2,4) * -1
        ball_vel[1] = random.randrange(1,3) * -1
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

   
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, WIDTH, HALF_PAD_HEIGHT, HALF_PAD_WIDTH
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
 
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    

    # 4. Modify your code such that the ball collides with and bounces
    # off of the top and bottom walls.
    # let ball bounce from top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        #top
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        #bottom
        ball_vel[1] = - ball_vel[1]
    
        
    # 1. draw ball 
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "#669fb2")
    
    ##############
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # END update paddles
    #
    ##############
    
    ##############
    # START draw paddles

    # left paddle
    #canva.draw_line((8/2, 200 - 40), (8/2, 200 + 40))
    canvas.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'Red')
    
    # right paddle((600 - 8/2, 200 - 40)), (600 - 8/2, 200 + 40))
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'Blue')
    
    # END draw paddles
    #
    ###############
    
    # draw scores

###############
# moving the paddles 

# on keydown paddles move in one direction
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 1
    if key==simplegui.KEY_MAP["down"]: # move left paddle down
        paddle1_vel += acc
    if key==simplegui.KEY_MAP["up"]: # move right paddle up
        paddle1_vel -= acc
    
    if key==simplegui.KEY_MAP["s"]: # move right paddle down
        paddle2_vel += acc
    if key==simplegui.KEY_MAP["w"]: # move right paddle up
        paddle2_vel -= acc

# on keyup paddles stop moving   
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 1
    if key==simplegui.KEY_MAP["down"]: # stop left paddle down movement
        paddle1_vel -= acc
    if key==simplegui.KEY_MAP["up"]: # stop left paddle up movement
        paddle1_vel += acc

    if key==simplegui.KEY_MAP["s"]: # stop right paddle down movement
        paddle2_vel -= acc
    if key==simplegui.KEY_MAP["w"]: # stop right paddle up movement
        paddle2_vel += acc        
    
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
