#!
#
# Setting up new wiring. Testing leds Red, Yellow, Green.

import RPi.GPIO as IO
import time, os, sys, random

IO.setmode(IO.BCM)

RED = 26
YELLOW = 21
GREEN = 20

LEDS = [26, 21, 20]

for i in LEDS:
    IO.setup(i, IO.OUT)

try:
    while True:
        for i in LEDS:
            IO.output(i, 1)
            time.sleep(0.2)
            IO.output(RED, 0)
        for i in LEDS:
            IO.output(i, 0)
except KeyboardInterrupt:
    IO.cleanup()
