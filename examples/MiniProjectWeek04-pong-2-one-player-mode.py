#-----------------------------------------------------------
# Implementation of classic arcade game Pong
#
# Additional Functions for abit of fun:
# - The players can add there names
# - A single player option which sincs both paddles with 
#   the Up and Down arrows
#-----------------------------------------------------------
#    Date      Ver   Comments
# ----------  -----  ----------------------------------------
# 18/10/2014   1.00   Initial code to test source.
#-----------------------------------------------------------

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
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_x = PAD_WIDTH / 2
paddle2_x = WIDTH - (PAD_WIDTH / 2)
ball_vel = [0, 0]
font_size = 30
starting = True
score1 = 0
score2 = 0
player1_name = "Player 1"
player2_name = "Player 2"
sinc_paddles = False

# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global ball_pos, ball_vel # these are vectors stored as lists
    global LEFT
    global score1, score2, starting

    # Replace the ball in the centre
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # Calculate the new randow direction to move
    # Not sure if '/60' is corrext, but I get the speeds I was after
    x = random.randrange(120,240)/60
    y = random.randrange(60,180)/60

    # if LEFT is True, then the ball's velocity is upper left    
    # if LEFT is False, then the ball's velocity is upper right
    # increment the score for the winner of the last game
    if LEFT == True:
        ball_vel[0] = - x
        score1 += 1
    else:
        ball_vel[0] = x
        score2 += 1
        
    # set the ball movement upward
    ball_vel[1] = - y
    
    # new game initialisation for paddles and scores
    if starting == True:
        paddle1_pos = (HEIGHT / 2)
        paddle1_vel = 0
        paddle2_pos = (HEIGHT / 2)
        paddle2_vel = 0
        
        score1 = 0
        score2 = 0
        
        starting = False

# define event handlers
def new_game():
    global starting
    
    # Set the new game indicator for the spawn process
    starting = True
    # Update the game controls as new game
    spawn_ball()
    
def draw(canvas):
    global score1, score2 
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    global LEFT, font_size
    global player1_name, player2_name
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball - horizontal position
    ball_pos[0] += ball_vel[0]

    # check if the ball has reached the gutter
    if ball_pos[0] <= 0 + PAD_WIDTH + BALL_RADIUS:
        # set the direction for the new ball if not paddled
        LEFT = False
        
        # Check if the ball hit the Left paddle
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
                # Paddle hit and ball velocity increased by 10%
                ball_vel[0] = - ball_vel[0]
                
                ball_vel[0] = ball_vel[0] * 1.1
            else:
                # Missed Paddle - spawn new ball
                spawn_ball()
        else:
            # Missed Paddle - spawn new ball
            spawn_ball()

    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        # set the direction for the new ball if not paddled
        LEFT = True

        # Check if the ball hit the Right paddle
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
                # Paddle hit and ball velocity increased by 10%
                ball_vel[0] = - ball_vel[0]
                
                ball_vel[0] = ball_vel[0] * 1.1
            else:
                # Missed Paddle - spawn new ball
                spawn_ball()
        else:
            # Missed Paddle - spawn new ball
            spawn_ball()
         
    # update ball vertical position        
    ball_pos[1] += ball_vel[1]

    # bounce ball of top or bottom borders
    if ball_pos[1] <= BALL_RADIUS:
            ball_vel[1] = - ball_vel[1]

    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
            ball_vel[1] = - ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'Yellow', 'Orange')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # stop Left paddle movement of the boundary edge has been reached
    if paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_vel = 0
    elif paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel = 0
    
    # stop Right paddle movement of the boundary edge has been reached    
    if paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_vel = 0
    elif paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_vel = 0
    
    # draw paddles
    canvas.draw_line([paddle1_x, paddle1_pos  - HALF_PAD_HEIGHT], [paddle1_x, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH , "White")
    canvas.draw_line([paddle2_x, paddle2_pos  - HALF_PAD_HEIGHT], [paddle2_x, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH , "White")
    
    # draw players name centred on each side
    len1 = frame.get_canvas_textwidth(player1_name, font_size)
    canvas.draw_text(player1_name,[(1.0*WIDTH/4) - (len1/2.0),font_size],font_size,"Red")        
    len2 = frame.get_canvas_textwidth(player2_name, font_size)
    canvas.draw_text(player2_name,[(3.0*WIDTH/4) - (len2/2.0),font_size],font_size,"Blue")        

    # draw scores
    canvas.draw_text(str(score1),[(1.0*WIDTH/4),font_size*2],font_size,"White")        
    canvas.draw_text(str(score2),[(3.0*WIDTH/4),font_size*2],font_size,"White")        
    
def keydown(key):
    global paddle1_vel, paddle2_vel, ball_vel
    global sinc_paddle
    
    # move paddles up or down while keys pressed
    if sinc_paddles == False:
        if key == simplegui.KEY_MAP["up"]:
            paddle2_vel = -3
            
        if key == simplegui.KEY_MAP["down"]:
            paddle2_vel = 3
        
        if chr(key) == "W":
            paddle1_vel = -3
            
        if chr(key) == "S":
            paddle1_vel = 3
    else:
        # move both paddles up or down while keys pressed
        if key == simplegui.KEY_MAP["up"]:
            paddle1_vel = -3            
            paddle2_vel = -3
            
        if key == simplegui.KEY_MAP["down"]:
            paddle1_vel = 3            
            paddle2_vel = 3
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    # stop paddle movement when key is released
    if sinc_paddles == False:
        if key == simplegui.KEY_MAP["up"]:
            paddle2_vel = 0
            
        if key == simplegui.KEY_MAP["down"]:
            paddle2_vel = 0
        
        if chr(key) == "W":
            paddle1_vel = 0
            
        if chr(key) == "S":
            paddle1_vel = 0
    else:
        # stop both paddles movement when key is released
        if key == simplegui.KEY_MAP["up"]:
            paddle1_vel = 0            
            paddle2_vel = 0

        if key == simplegui.KEY_MAP["down"]:
            paddle1_vel = 0            
            paddle2_vel = 0

def player1(name):
    global player1_name
    
    #set player 1's name on the board
    player1_name = name

def player2(name):
    global player2_name
    
    #set player 2's name on the board
    player2_name = name

def lock_paddles():
    global sinc_paddles, paddle1_pos, paddle2_pos
    
    if lock.get_text() == "Single Player - Up Down Arrows Only.":
        sinc_paddles = True
        paddle1_pos = paddle2_pos
        lock.set_text("Two Player - 'W' 'S' keys activate")
    else:
        sinc_paddles = False
        lock.set_text("Single Player - Up Down Arrows Only.")

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Game Reset button
frame.add_button("Reset", new_game)

# Players name input
inp1 = frame.add_input("Player 1 - Name", player1, 200)
inp1.set_text(player1_name)
inp2 = frame.add_input("Player 2 - Name", player2, 200)
inp2.set_text(player2_name)

# Single Player and Paddle sinc lock button
lock = frame.add_button("Single Player - Up Down Arrows Only.", lock_paddles)

# start frame
new_game()
frame.start()

