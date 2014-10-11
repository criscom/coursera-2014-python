# template for "Stopwatch: The Game"

import simplegui

# define global variables

#variable for incrementing the timer
t = 0

#variable for the display of the stopwatch
time = "0"

#variable for counting the clicks on stop
click = 0

#variable for counting successful clicks
success = 0

#variable for displaying the score

score = "0 / 0"

#is timer running or not
started = False

#position for the timer on the canvas
position_stopwatch = [105,150]

#position for the score on the canvas
position_score = [230,30]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    # last digit or tenth of a seconds
    # ex. 723 tenths of a second
    # 723 % 10 = 3
    # D = 3
    D = t % 10

    # second but last digit or seconds
    # 723 // 10 = 72
    # 72 % 60 = 12
    # 12 % 10 = 2
    # C = 1
    C = ((t // 10) % 60) % 10

    # third but last digit or tens of seconds
    # 12 // 10 = 1
    # B = 1
    B = ((t // 10) % 60) // 10
    
    # 723 // 600 = 1
    # A = 1
    A = t // 600

    # Stopp watch output as string
    # t = A:BC.D
    # 723 = 1:12.3
    time = str(A)+":"+str(B)[0]+str(C)[0]+"."+str(D)
    return time

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global started
    timer.start()
    started = True

def stop_timer():
    global started, click, success, score
    if started == True:
       timer.stop()
       started = False
       click += 1
       if (t % 10) == 0:
          success +=1
    score = str(success)+" / "+str(click)
    return score
    

def reset_timer():
    global t, started, click, success, score
    if started:
       timer.stop()
    t = 0
    click = 0
    success = 0
    score = str(success)+" / "+str(click)
    return score
       

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1


# define draw handler
def draw(canvas):
    format(t)
    canvas.draw_text(time, position_stopwatch, 36, "#003465")
    canvas.draw_text(score, position_score, 28, "#15cd30")

    
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
