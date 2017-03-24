import simplegui
import random
import math
qty=int(input('number of balls to simulate'))
pointx=int(input("enter the x reference"))
pointy=int(input("enter the y reference"))
pt1=[None]*qty
pt2=[None]*qty
velo1=[None]*qty
velo2=[None]*qty
i=0
j=0
theta=0
change=0
ctr=0
time=1
for i in range(qty):  #never check for collision with equating points because if velo inc. by each iteration it is possible that point pos becomes greater suddenly hence no collision
    pt1[i]=pointx+random.randint(-pointx,500-pointx)
    pt2[i]=pointy+random.randint(-pointy,500-pointy)
    velo1[i]=random.choice([-1,1])
    velo2[i]=random.choice([-1,1])
    
def draw(canvas): 
    global pt1,pt2,velo,change,ctr,i,j 
    i=0
    j=0
    for i in range(qty):     #if you use for loop it will happen unlimited times as in event driven programming handlers is called again and again
                             #even in case of while draw inside canvas wont be printed because while for 1st time handler call does its part but then next time no while so no retracing
        
        pt1[i]+=velo1[i]
        pt2[i]+=velo2[i]
        if i==ctr:
            canvas.draw_circle([pt1[i],pt2[i]],2,5,"red")
        else:
            canvas.draw_circle([pt1[i],pt2[i]],2,5,"Fuchsia")
        if pt1[i]<=2 or (500-(pt1[i])<=2): 
            velo1[i]=-velo1[i]
            #canvas.draw_circle([pt1[i],pt2[i]],2,5,"Fuchsia")
        if pt2[i]<=2 or (500-(pt2[i]))<=2:
            velo2[i]=-velo2[i]
            #canvas.draw_circle([pt1[i],pt2[i]],2,5,"Fuchsia")
        for j in range(qty):
            if i!=j:
                if math.sqrt(math.pow((pt2[i]-pt2[j]),2)+math.pow((pt1[i]-pt1[j]),2))<=4:
                    check()
                    
def check():
    global velo1,velo2,pt1,pt2,i,j
    theta=math.degrees(math.atan((pt2[i]-pt2[j])/(pt1[i]-pt2[j])))
    velo1[i]=-velo1[i]*(math.cos(theta))
    velo2[i]=-velo2[i]*(math.sin(theta))
def tick():     
    global time
    time=time+1
def key_handler(key):
    global time
    if key==simplegui.KEY_MAP["h"]:
        change=1
        for i in range(qty):
            if velo1[i]>0 and velo2[i]>0:
                velo1[i]+=time
                velo2[i]+=time
            elif velo1[i]<0 and velo2[i]<0:
                velo1[i]-=time
                velo2[i]-=time
            elif velo1[i]<0 and velo2[i]>0:
                velo1[i]-=time
                velo2[i]+=time
            else:
                velo1[i]+=time
                velo2[i]-=time
    
def click(pos):
    global ctr
    ctr+=1
    if ctr>qty or ctr==qty:
        ctr=0
        
frame=simplegui.create_frame("collision simulator",500,500)
timer=simplegui.create_timer(1000,tick)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
frame.set_mouseclick_handler(click)
frame.start()
if change==1:
    timer.start()
