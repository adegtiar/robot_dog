import time
import digitalio
import board

orange = digitalio.DigitalInOut(board.LED_ORANGE)
orange.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.LED_GREEN)
green.direction = digitalio.Direction.OUTPUT
red = digitalio.DigitalInOut(board.LED_RED)
red.direction = digitalio.Direction.OUTPUT
blue = digitalio.DigitalInOut(board.LED_BLUE)
blue.direction = digitalio.Direction.OUTPUT

#colorlist = ["orange","green","red","blue"]
speed = 0.05
while True:
    red.value = True
    time.sleep(speed)
    red.value = False
    time.sleep(speed)
    
    blue.value = True
    time.sleep(speed)
    blue.value = False
    time.sleep(speed)
    
    green.value = True
    time.sleep(speed)
    green.value = False
    time.sleep(speed)
    
    orange.value = True
    time.sleep(speed)
    orange.value = False
    time.sleep(speed)
    

    

    


