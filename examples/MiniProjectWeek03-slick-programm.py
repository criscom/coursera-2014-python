# template for "Stopwatch: The Game"

import simplegui

# define global variables
width = 300
height = 200
time_interval = 100
c1 = 0
c2 = " "
sec = 0
minute = 0
wins = 0
count = 0
score ="0/0"
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global c1,c2
    c2 = str(c1)
    tick()
    timer.start()


def Stop():
    global c1,c2,wins,count,score
    c2 = str(c1)
    timer.stop()
    if c1 == 0:
        wins += 1
        count+=1
    else:
        count+=1
    score = str(wins)+"/"+ str(count)
    
def Reset():
    global c1,c2,sec,minute,wins,count,score
    c1 = 0
    sec = 0
    minute = 0
    wins = 0
    count = 0
    c2 = str(c1)
    timer.stop()
    score = str(wins)+"/"+ str(count)

# define event handler for timer with 0.1 sec interval
def tick():
    global c1, sec, minute
    if c1 >= 0:
       c1 = c1 + 1
       if c1 == 10:
            c1 = 0
            sec = sec + 1
            if sec == 60:
                sec = 0
                minute = minute + 1
                if minute == 61:
                    c1 = 0
                    sec = 0
                    minute = 0
        
timer = simplegui.create_timer(time_interval,tick)

# define draw handler
def draw(canvas):
    global c1,score
    c2=str(c1)
    if (len(str(sec))==1):
        c4=str(minute) + ":0" + str(sec) + "." + str(c2)
    else:
        c4=str(minute) + ":" + str(sec) + "." + str(c2)
    canvas.draw_text(c4, [110,110], 40, "White")
    canvas.draw_text(score, [230,30], 30, 'Green')
    


    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game",width,height)
frame.add_button('Start',Start,100)
frame.add_button('Stop',Stop,100)
frame.add_button('Reset',Reset,100)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
