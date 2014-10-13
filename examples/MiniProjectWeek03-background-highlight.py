import simplegui
 
# define global variables
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 130
time = 0
attempts = 0
success = 0
 
def init():
    global time, attempts, success
    time = 0
    attempts = 0
    success = 0
 
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = str(t // 600)
    secs = str(t % 600)
    while len(secs) < 3:
        secs = "0" + secs
    return minutes + ":" + secs[:-1] + "." + secs[-1]
 
def mark_attempt():
    global attempts, success
    if timer.is_running():
        attempts += 1
    if not time % 10:
        success += 1
 
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
 
def stop():
    mark_attempt()
    timer.stop()
 
def reset():
    stop()
    init()
 
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
 
# define draw handler
def draw(canvas):
    
# highlight background each second
    if not time % 10:
        frame.set_canvas_background("#D3D3D3") # light gray
    else:
        frame.set_canvas_background("Silver")
    
# draw success/attempts
    text = str(success) + " / " + str(attempts)
    text_width = frame.get_canvas_textwidth(text, 16, "sans-serif")
    posx = CANVAS_WIDTH - text_width - 6
    canvas.draw_text(text, (posx, 22), 16, "Gray", "sans-serif")

# draw counter
    counter = format(time)
    counter_width = frame.get_canvas_textwidth(counter, 48, "sans-serif")
    posx = (CANVAS_WIDTH - counter_width) // 2
    canvas.draw_text(counter, (posx, (CANVAS_HEIGHT + 24) // 2),
                     48, "Black" )
 
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",
                CANVAS_WIDTH, CANVAS_HEIGHT)
timer = simplegui.create_timer(100, tick)
 
# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)
 
# start frame
frame.start()