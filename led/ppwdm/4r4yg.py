#!
#
# Setting up new wiring. Testing leds Red, Yellow, Green.

import RPi.GPIO as IO
import time, os, sys, random

IO.setmode(IO.BCM)

RED = 26
YELLOW = 21
GREEN = 20
R1 = 13
R2 = 6
R3 = 12
Y1 = 7
Y2 = 8
Y3 = 11

LEDS = [26, 21, 20, 13, 6, 12, 7, 8, 11 ]

for i in LEDS:
    IO.setup(i, IO.OUT)

try:
    while True:
        for i in LEDS:
            IO.output(i, 1)
            time.sleep(0.2)
        IO.output(LEDS, 0)
        time.sleep(0.2)
except KeyboardInterrupt:
    IO.cleanup()
