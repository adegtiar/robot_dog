#python
#circuitpython

#impstanding_pose = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
#ort board
#import time
#from adafruit_motor import servo

#FIXED ACTIONS
standing_pose = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
sitting_pose    = {"FLL":90,"FRL":90,"HLL":0,"HRL":180}
play_pose       = {"FLL":45,"FRL":130,"HLL":90,"HRL":90}
tail_wag        = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
walk_s1         = {"FLL":0,"FRL":90,"HLL":90,"HRL":90}
walk_s2         = {"FLL":90,"FRL":0,"HLL":90,"HRL":90}
walk_s3         = {"FLL":90,"FRL":90,"HLL":0,"HRL":90}
walk_s4         = {"FLL":90,"FRL":90,"HLL":90,"HRL":0}

#BEHAVIOR
direction = ["fwd","back","left","right"]
steps = range(0,100)
speed = range(0,100)
#Accel
#Decel

#take in dirrection and speed and apply to a sequence of moments that move the
#animal in the dirrection and speed requested.

def move(d,sTp,sPd):
    if(d == "fwd"):
        print("forward walk ",sTp," steps at",sPd," speed")
    if(d == "back"):
        print("backward walk ",sTp," steps at",sPd," speed")
    if(d == "left"):
        print("left walk ",sTp, "steps at",sPd," speed")
    if(d == "right"):
        print("right walk ",sTp," steps at",sPd," speed")
    
def speak(tone,loudness,purpose):

    pass
#if someone is in the room go to them and sit as close as possible to them.

def find(thing, howLong):
    pass
    #move in a random pattern allowing the room to develop the pattern of search.
    #when found small short whine
    #if not found after how long
    #go to another room, or return to doghouse
    #fail to find then doghouse


#if no-body in the room, go to doghouse and charge/dataUP

#When x time has passed go find something on the ground and bring it to them.

#If voice command, do then after 5 min bark, if no command, return to main.

move(direction[1],steps[10],speed[30])
