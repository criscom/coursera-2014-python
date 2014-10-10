# template for "Stopwatch: The Game"

import simplegui

# define global variables

#variable for incrementing the timer
interval = 100

t = "0"

#position of the timer on the canvas
position = [150,150]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()

def stop_timer():
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global interval
    global t
    interval += 1
    t = str(interval)
    return t

# define draw handler
def draw(canvas):
    canvas.draw_text(t, position, 36, "#003465")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300, 200)

# give frame a background
frame.set_canvas_background("White")

# register event handlers

#register draw handler
frame.set_draw_handler(draw)

#create start button
frame.add_button('Start timer', start_timer, 200)

#create stop button
frame.add_button('Stop timer', stop_timer, 200)

# create timer
timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()
# start timer

# Please remember to review the grading rubric
