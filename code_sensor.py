import time
import board
import pwmio
from adafruit_motor import servo
import busio
import adafruit_mpr121

#i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.PA08, board.PC09)
mpr121 = adafruit_mpr121.MPR121(i2c)

flag = 1

while flag == 1:
    print("Testing")

    for i in range(12):
        if mpr121[i].value:
            print("Pin {} touched!".format(i))
            flag = 2
            break

            
            

