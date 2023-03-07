#python
#circuitpython

import board
import digitalio
import time
from adafruit_motor import servo
import pwmio


#impstanding_pose = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
#ort board
#import time
#from adafruit_motor import servo

#FIXED ACTIONS
standing_pose = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
sitting_pose    = {"FLL":90,"FRL":90,"HLL":0,"HRL":180}
play_pose       = {"FLL":45,"FRL":130,"HLL":90,"HRL":90}
tail_wag        = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
walk_s1         = {"FLL":45,"FRL":90,"HLL":90,"HRL":90}
walk_s2         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
walk_s3         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}
walk_s4         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
walk_s5         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}

#BEHAVIOR
direction = ["fwd","back","left","right"]
steps = range(0,100)
speed = range(0,100)
#Accel
#Decel

#take in dirrection and speed and apply to a sequence of moments that move the
#animal in the dirrection and speed requested.

myservoFL = servo. Servo(pwm)
myservoFR = servo. Servo(pwm2)
myservoHL = servo. Servo(pwm3)
myservoHR = servo. Servo(pwm17)

#led = digitalio.DigitalInOut(board.LED)
#led.direction = digitalio.Direction.OUTPUT

def move(d,sTp,sPd):
    if(d == "fwd"):
        #s1 #walk_s1         = {"FLL":45,"FRL":90,"HLL":90,"HRL":90}
        myservoFL.angle = 90 # 0 -> 45
        led.value = True
        time.sleep(1)
        #s2 #walk_s2         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
        led.value = False
        myservoHR.angle = 90 # 0 ->45
        time.sleep(1)     
        #s3  #walk_s3         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}
        led.value = True
        myservoFR.angle = 90 # 0 -> 135    
        myservoHL.angle = 90 # 0 -> 135     
        time.sleep(1)
        #s4 #walk_s4         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
        led.value = False
        myservoFL.angle = 90 # 0 ->45
        myservoHR.angle = 90 # 0 ->45        
        time.sleep(1) 
        #s5  #walk_s5         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}
        led.value = True
        myservoFR.angle = 90 # 0 -> 135   
        myservoHL.angle = 90 # 0 -> 135           
        time.sleep(1)        
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
led = digitalio.DigitalInOut(board.LED_BLUE)
led.direction = digitalio.Direction.OUTPUT

pwm = pwmio.PWMOut(board.PA01, duty_cycle=2**15, frequency = 50)
pwm2 = pwmio.PWMOut(board.GP2, duty_cycle=2**15, frequency = 50)
pwm3 = pwmio.PWMOut(board.GP3, duty_cycle=2**15, frequency = 50)
pwm17 = pwmio.PWMOut(board.GP17, duty_cycle=2**15, frequency = 50)



move(direction[1],steps[10],speed[30])
