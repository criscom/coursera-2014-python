# template for "Stopwatch: The Game"

import simplegui

# define global variables

#variable for incrementing the timer
t = 0

time = "0"

#variable for the format

#is timer running or not
started = False

#position of the timer on the canvas
position = [105,150]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    # last digit or tenth of a seconds
    D = t % 10
    # second but last digit or seconds
    C = ((t // 10) % 60) % 10
    # third but last digit or tens of seconds
    B = ((t // 10) % 60) // 10
    A = t // 600
    time = str(A)+":"+str(B)[0]+str(C)[0]+"."+str(D)
    return time

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global started
    timer.start()
    started = True

def stop_timer():
    global started
    timer.stop()
    started = False

def reset_timer():
    global t
    global started
    if started:
       timer.stop()
    t = 0
       

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1


# define draw handler
def draw(canvas):
    format(t)
    canvas.draw_text(time, position, 36, "#003465")
    
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

#create reset button
frame.add_button('Reset timer', reset_timer, 200)

# create timer
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
# start timer

# Please remember to review the grading rubric
