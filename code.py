import board
import digitalio
import time
from adafruit_motor import servo
import pwmio

pwm = pwmio.PWMOut(board.GP15, duty_cycle=2**15, frequency = 50)

myservo = servo. Servo(pwm)
#myservo1 = servo. Servo(pwm)
#myservo1 = servo. Servo(pwm)
#myservo1 = servo. Servo(pwm)
#ask about pin 17 in discord


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT



while True:
    myservo.angle = 90 # 0 -> 180
    led.value = True
    time.sleep(3)
    led.value = False
    myservo.angle = 180
    time.sleep(3)
