# template for "Stopwatch: The Game"
import simplegui

# define global variables
count=0
attempts=0
sattempts=0
flag=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    A=t//600
    temp1=t//10
    temp2=temp1%60
    B=temp2//10
    C=temp2%10
    D=t%10
    return str(A)+':'+str(B)+str(C)+'.'+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start() :
    global flag
    flag=True
    timer.start()
    
def stop():
    global attempts,flag,sattempts
    
    if flag and count % 10 == 0 :
        sattempts+=1
        
    
    if flag==True:
        attempts+=1
        
    flag=False
    
    
    timer.stop()
    
def reset():
    global count,attempts,sattempts
    count=0
    attempts=0
    sattempts=0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def interval():
    global count
    count+=1
   

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count),[110,150],35,"white")
    canvas.draw_text(str(sattempts)+"/"+str(attempts),[240,40],30,"yellow")
    
    
# create frame
frame=simplegui.create_frame("StopWatch",300,300)

# register event handlers
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)

timer=simplegui.create_timer(100,interval)

# start frame
frame.start()


# Please remember to review the grading rubric
