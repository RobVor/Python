#!
#
# Getting PiLITEr to work and testing modulation through GPIO.PWM

import RPi.GPIO as IO
import time, os

leds = [4, 17 ,18, 22, 23, 24, 25]

IO.setmode(IO.BCM)
try:
    while True:
        for i in range(1, 41):
            IO.setup(i, IO.OUT)
            IO.output(i, 1)
            print("This is GPIO pin " + str(i))
            time.sleep(1.5)
            IO.output(i, 0)
#        for i in leds:
#            IO.setup(i, IO.OUT)
#        IO.output(leds, 1)
except KeyboardInterrupt:
    IO.cleanup()
    exit()
