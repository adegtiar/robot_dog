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

ANGLE_DELTA = 40


standing_pose = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
sitting_pose    = {"FLL":90,"FRL":90,"HLL":0,"HRL":180}
play_pose       = {"FLL":45,"FRL":130,"HLL":90,"HRL":90}
tail_wag        = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
"""
walk_s1         = {"FLL":45,"FRL":90,"HLL":90,"HRL":90}
walk_s2         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
walk_s3         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}
walk_s4         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
walk_s5         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}
"""
"""
walk_s1         = {"FLL":90-ANGLE_DELTA,"FRL":90,"HLL":90,"HRL":90}
walk_s2         = {"FLL":90-ANGLE_DELTA,"FRL":90,"HLL":90,"HRL":90+ANGLE_DELTA}
walk_s3         = {"FLL":90,"FRL":90+ANGLE_DELTA,"HLL":90-ANGLE_DELTA,"HRL":90}
walk_s4         = {"FLL":90-ANGLE_DELTA,"FRL":90,"HLL":90,"HRL":90+ANGLE_DELTA}
walk_s5         = {"FLL":90,"FRL":90+ANGLE_DELTA,"HLL":90-ANGLE_DELTA,"HRL":90}
walk_orientations = [walk_s1, walk_s2, walk_s3, walk_s4, walk_s5]
"""
walk_s1a         = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
walk_s1b         = {"FLL":80,"FRL":90,"HLL":90,"HRL":90}
walk_s1c         = {"FLL":70,"FRL":90,"HLL":90,"HRL":90}
walk_s1d         = {"FLL":60,"FRL":90,"HLL":90,"HRL":90}
walk_s1e         = {"FLL":50,"FRL":90,"HLL":90,"HRL":90}

walk_s2a         = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
walk_s2b         = {"FLL":80,"FRL":90,"HLL":90,"HRL":100}
walk_s2c         = {"FLL":70,"FRL":90,"HLL":90,"HRL":110}
walk_s2d         = {"FLL":60,"FRL":90,"HLL":90,"HRL":120}
walk_s2e         = {"FLL":50,"FRL":90,"HLL":90,"HRL":130}

walk_s3a         = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
walk_s3b         = {"FLL":90,"FRL":100,"HLL":80,"HRL":90}
walk_s3c         = {"FLL":90,"FRL":110,"HLL":70,"HRL":90}
walk_s3d         = {"FLL":90,"FRL":120,"HLL":60,"HRL":90}
walk_s3e         = {"FLL":90,"FRL":130,"HLL":50,"HRL":90}

walk_s4a         = {"FLL":90,"FRL":90,"HLL":90,"HRL":90}
walk_s4b         = {"FLL":80,"FRL":90,"HLL":90,"HRL":100}
walk_s4c         = {"FLL":70,"FRL":90,"HLL":90,"HRL":110}
walk_s4d         = {"FLL":60,"FRL":90,"HLL":90,"HRL":120}
walk_s4e         = {"FLL":50,"FRL":90,"HLL":90,"HRL":130}

walk_s5         = {"FLL":90,"FRL":90+ANGLE_DELTA,"HLL":90-ANGLE_DELTA,"HRL":90}



walk_orientations = [walk_s1a, walk_s1b, walk_s1c, walk_s1d, walk_s1e,walk_s2a,walk_s2b,walk_s2c,walk_s2d,walk_s2e,walk_s3a,walk_s3b,walk_s3c,walk_s3d,walk_s3e, walk_s4a, walk_s4b, walk_s4c, walk_s4d, walk_s4e, walk_s5]
#walk_orientations = [walk_s1e,walk_s2e,walk_s3e,walk_s4e,walk_s5]
Bwalk_s1         = {"FLL":90-ANGLE_DELTA,"FRL":90,"HLL":90,"HRL":90}
Bwalk_s2         = {"FLL":90-ANGLE_DELTA,"FRL":90,"HLL":90,"HRL":90+ANGLE_DELTA}
Bwalk_s3         = {"FLL":90,"FRL":90+ANGLE_DELTA,"HLL":90-ANGLE_DELTA,"HRL":90}
Bwalk_s4         = {"FLL":90-ANGLE_DELTA,"FRL":90,"HLL":90,"HRL":90+ANGLE_DELTA}
Bwalk_s5         = {"FLL":90,"FRL":90+ANGLE_DELTA,"HLL":90-ANGLE_DELTA,"HRL":90}
Bwalk_orientations = [Bwalk_s1, Bwalk_s2, Bwalk_s3, Bwalk_s4, Bwalk_s5]

#BEHAVIOR
direction = ["fwd","back","left","right"]
steps = range(0,100)
speed = range(0,100)
#Accel
#Decel

LEFT_FRONT_PIN = board.PA02
RIGHT_FRONT_PIN = board.PA01
LEFT_BACK_PIN = board.PB09
RIGHT_BACK_PIN = board.PA03

# TODO: make this less duplicated coded


"""
def init_servo(pin: board.Pin) -> servo.Server:
    pwm = pwmio.PWMOut(pin, duty_cycle=2**15, frequency = 50)
    return servo.Servo
#take in dirrection and speed and apply to a sequence of moments that move the
#animal in the dirrection and speed requested.
SERVOS = {
    "FLL": init_servo(LEFT_FRONT_PIN),
    "FRL": init_servo(RIGHT_FRONT_PIN),
    "HLL": init_servo(LEFT_BACK_PIN),
    "HRL": init_servo(RIGHT_BACK_PIN),
}
myservoFL = SERVOS["FLL"]
myservoFR = SERVOS["FRL"]
myservoHL = SERVOS["HLL"]
myservoHR = SERVOS["HRL"]
"""

def init_pwm(pin: board.Pin) -> servo.Server:
    return pwmio.PWMOut(pin, duty_cycle=2**15, frequency = 50)


left_front_pwm = init_pwm(board.PA02)
right_front_pwm = init_pwm(board.PA01)
left_back_pwm = init_pwm(board.PB09)
right_back_pwm = init_pwm(board.PA03)


right_front_leg = servo.Servo(right_front_pwm)
left_front_leg = servo.Servo(left_front_pwm)
right_back_leg = servo.Servo(right_back_pwm)
left_back_leg = servo.Servo(left_back_pwm)

myservoFL = left_front_leg
myservoFR = right_front_leg
myservoHL = left_back_leg
myservoHR = right_back_leg

LEGS = {
    "FLL": left_front_leg,
    "FRL": right_front_leg,
    "HLL": left_back_leg,
    "HRL": right_back_leg,
}


#led = digitalio.DigitalInOut(board.LED)
#led.direction = digitalio.Direction.OUTPUT

def update_legs(orientations):
    for leg_id, angle in orientations.items():
        LEGS[leg_id].angle = angle


def move(d,sTp,sPd):
    if(d == "fwd"):
        #s1 #walk_s1         = {"FLL":45,"FRL":90,"HLL":90,"HRL":90}
        for walk_orientation in walk_orientations:
            update_legs(walk_orientation)
            input()
            #time.sleep(1)
        """
        LEGS["FLL"].angle = 90 # 0 -> 45
        led.value = True
        time.sleep(1)
        #s2 #walk_s2         = {"FLL":45,"FRL":90,"HLL":90,"HRL":45}
        led.value = False
        myservoHR.angle = 135 # 0 ->45
        time.sleep(1)
        #s3  #walk_s3         = {"FLL":90,"FRL":135,"HLL":135,"HRL":90}
        led.value = True
        myservoFR.angle = 135 # 0 -> 135
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
        """
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


update_legs(standing_pose)
time.sleep(1)
while True:
    move(direction[0],steps[10],speed[30])
