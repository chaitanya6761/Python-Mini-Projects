# implementation of card game - Memory
#codeskluptor link: http://www.codeskulptor.org/#user40_Xr1Ak2FH0Q2JZay.py

import simplegui
import random

list1=[]
list2=[]
finalList=[]
exposed=[]
state=0
pos1=0
pos2=0
turns=0

# helper function to initialize globals
def new_game():
    global list1,list2,finalList,exposed,state,pos1,pos2,turns
    
    list1=range(0,8)
    list2=range(0,8)
    finalList=list1+list2
    random.shuffle(finalList)
    exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    state=0
    pos1=0
    pos2=0
    turns=0
                              
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    xcor=10
    ycor=60
    a = 0
    b = 0
    width =50 
    height = 100
    
    
    for num in finalList :
        canvas.draw_text(str(num),[xcor,ycor],40,"white")
        xcor+=50
        
    for val in exposed :
        
        if not val :
            canvas.draw_polygon([(a, b), (a, b + height), (a + width, b + height), (a + width, b)], 1, "red","green")

        a+=50
        
        label.set_text("Turns = "+str(turns))
        
        
def mouseclick(key):
    global state,finalList,pos1,pos2,turns
    list_key=list(key)
    #print list_key
    
    temp_pos=list_key[0]/50
    
    if state == 0:
        state = 1
        
        pos1=temp_pos
        exposed[pos1]=True
        
        
        
    elif state == 1:
        
        if exposed[temp_pos] == False:
            state = 2
            pos2=temp_pos
            exposed[pos2]=True
            turns+=1
        
        
        
        
    else:
        
        if exposed[temp_pos] == False:
            state = 1
        
            if finalList[pos1]!=finalList[pos2] :
                exposed[pos1]=exposed[pos2]=False
            
            pos1=temp_pos
            exposed[pos1]=True
        
                  
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



