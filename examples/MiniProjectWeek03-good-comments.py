# A stopwatch that tests your reflexes

import simplegui

# Global variables

t = 0
mins = "0"
tens = "0"
secs = "0"
tenths = "0"
stop_count = 0
win_count = 0
score = "0 / 0"
running = False

# Helper functions

def format(t):
    """
    converts time in tenths of seconds
    into formatted string A:BC.D
    """
    mins = str(t // 600)
    tens = str((t % 600) // 100)
    secs = str((t % 100) // 10)
    tenths = str(t % 10)
    return mins + ":" + tens + secs + "." + tenths

# Event handlers

# Event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global running
    timer.start()
    running = True

def stop():
    global running
    timer.stop()
    win_counter()

def reset():
    # Resets all
    global t, stop_count, win_count, score
    timer.stop()
    t = 0
    stop_count = 0
    win_count = 0
    score = "0 / 0"
    
def win_counter():
    # Counts your stops and stops on the second
    global stop_count, win_count, score, running
    if running:    # Only increases stop_count and (maybe) win_count if stopwatch is running
        stop_count += 1
        if (t % 10) == 0:    # Only increases win_count if t (deciseconds) / 10 leaves no remainder
            win_count +=1
    elif not(running):    # If stopwatch not running, passes (ignores) win_counter
        pass
    running = False
    score = str(win_count) + " / " + str(stop_count)
    
def timer_handler():
    # Event handler for timer with 0.1 sec interval
    global t
    if t < 6000:
        t += 1
    elif t == 6000:    # Limits timer duration to 6000 milliseconds (ten minutes)
        reset()

def draw_handler(canvas):
    canvas.draw_text(format(t), (10, 110), 40, "White")
    canvas.draw_text(score, (100, 40), 40, "Blue")

# Create frame

frame = simplegui.create_frame("Stopwatch", 200, 200, 50)

# Register event handlers

timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 60)
frame.add_button("Stop", stop, 60)
frame.add_button("Reset", reset, 60)

# Start frame

frame.start()