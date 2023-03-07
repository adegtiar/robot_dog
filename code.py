import board
import digitalio
import time
from adafruit_motor import servo
import pwmio

# Led used to debug and verify code is running.
led = digitalio.DigitalInOut(board.LED_BLUE)
led.direction = digitalio.Direction.OUTPUT

# PWM pins
# TODO: make this less duplicated coded
right_front_pwm = pwmio.PWMOut(board.PA01, duty_cycle=2**15, frequency = 50)
left_front_pwm = pwmio.PWMOut(board.PA02, duty_cycle=2**15, frequency = 50)
right_back_pwm = pwmio.PWMOut(board.PA03, duty_cycle=2**15, frequency = 50)
left_back_pwm = pwmio.PWMOut(board.PB09, duty_cycle=2**15, frequency = 50)

# Legs
right_front_leg = servo.Servo(right_front_pwm)
left_front_leg = servo.Servo(left_front_pwm)
right_back_leg = servo.Servo(right_back_pwm)
left_back_leg = servo.Servo(left_back_pwm)

legs = [right_front_leg, left_front_leg, right_back_leg, left_back_leg]
#ask about pin 17 in discord


def move_legs(angle):
    for leg in legs:
        leg.angle = angle


while True:
    move_legs(45)
    # Enable LED light
    led.value = True
    time.sleep(2)

    move_legs(0)
    led.value = False
    time.sleep(2)
