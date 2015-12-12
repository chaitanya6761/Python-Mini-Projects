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
ball_pos=[0,0]
ball_vel=[0,0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    
    if direction == RIGHT :
        ball_vel[0] = random.randrange(120, 240) / 60 
        ball_vel[1] = -random.randrange(60, 180) / 60
    
    elif direction == LEFT :
        ball_vel[0] = -random.randrange(120, 240) / 60 
        ball_vel[1] = -random.randrange(60, 180) / 60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    
    score1=0
    score2=0
    paddle1_pos=(HEIGHT-PAD_HEIGHT)/2  
    paddle2_pos=(HEIGHT-PAD_HEIGHT)/2
    paddle1_vel=0
    paddle2_vel=0
    spawn_ball(True)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH :
        
        if paddle1_pos <= ball_pos[1] <= paddle1_pos+PAD_HEIGHT :
            ball_vel[0]=-1.1*ball_vel[0]
       
        else :    
            spawn_ball(True)  
            score2+=1
   
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH :
        
        if paddle2_pos <= ball_pos[1] <= paddle2_pos+PAD_HEIGHT :
            ball_vel[0]=-1.1*ball_vel[0]
        
        else :
        
            spawn_ball(False)
            score1+=1
        
    
    
    elif ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS :
        ball_vel[1]=-ball_vel[1]
     
    
            
    # draw ball
    
    canvas.draw_circle(ball_pos,BALL_RADIUS,4,"white","white")
    
    
    # update paddle's vertical position, keep paddle on the screen
    
    
    if 0 <= (paddle1_pos+paddle1_vel) <= (HEIGHT - PAD_HEIGHT )  :
        paddle1_pos+=paddle1_vel
    
    if 0 <= (paddle2_pos+paddle2_vel) <= (HEIGHT - PAD_HEIGHT )  :
         paddle2_pos+=paddle2_vel
    
    # draw paddles
    canvas.draw_line([0,paddle1_pos],[0,paddle1_pos+PAD_HEIGHT],PAD_WIDTH*2,"white")
    canvas.draw_line([WIDTH-PAD_WIDTH/2,paddle2_pos],[WIDTH-PAD_WIDTH/2,paddle2_pos+PAD_HEIGHT],PAD_WIDTH,"white")
    
       
    # determine whether paddle and ball collide    
    
    
    
    
    # draw scores
    canvas.draw_text(str(score1), (150, 50), 50, 'white')
    canvas.draw_text(str(score2), (450, 50), 50, 'white')

    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == 87 :
        paddle1_vel -= 5
    
    elif key == 83 :
        paddle1_vel += 5
        
    elif key == 38 :
        paddle2_vel -= 5
        
    elif key == 40 :
        paddle2_vel += 5
    
    
def keyup(key):
   
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART",new_game)

# start frame
new_game()
frame.start()
