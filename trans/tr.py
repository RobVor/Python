#!
#
# tr.py - Testing of transistors and circuit design with them.

import RPi.GPIO as IO
import time, sys, os, random

IO.setmode(IO.BCM)
IO.setup(4, IO.OUT)
IO.output(4, 1)
print("Flash on")
time.sleep(0.5)
print("Flash off")
IO.output(4, 0)

LED = IO.PWM(4, 100)
LED.start(0)
try:
    while True:
        for i in range(100):
            LED.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(100, 0, -1):
            LED.ChangeDutyCycle(i)
            time.sleep(0.01)
except KeyboardInterrupt:
    IO.cleanup()
exit()
