#!
#
# Setting up new wiring. Testing leds Red, Yellow, Green.

import RPi.GPIO as IO
import time, os, sys, random

IO.setmode(IO.BCM)

#RED = 26
#YELLOW = 21
#GREEN = 20
R1 = 13
R2 = 6
R3 = 12
Y1 = 7
Y2 = 8
Y3 = 11
cycle = 0
nap = 0.5

#LEDS = [26, 21, 20, 13, 6, 12, 7, 8, 11]
PULSE = [13, 6, 12, 7, 8, 11]

for i in PULSE:
    IO.setup(i, IO.OUT)

while cycle < 500:
    print("Cycling @: " + str(cycle))
    print("Nap @: " + str(nap))
    cycle += 1
    if cycle == 100:
        nap -= 0.1
    elif cycle == 200:
        nap -= 0.1
    elif cycle == 300:
        nap -= 0.1
    elif cycle == 400:
        nap -= 0.1
    elif cycle == 450:
        nap == 0.01
    jump = random.randint(1, 6)
    time.sleep(nap)
    if jump == 1:
        IO.output(PULSE, 0)
        IO.output(R1, 1)
    elif jump == 2:
        IO.output(PULSE, 0)
        IO.output(R2, 1)
    elif jump == 3:
        IO.output(PULSE, 0)
        IO.output(R3, 1)
    elif jump == 4:
        IO.output(PULSE, 0)
        IO.output(Y1, 1)
    elif jump == 5:
        IO.output(PULSE, 0)
        IO.output(Y2, 1)
    elif jump == 6:
        IO.output(PULSE, 0)
        IO.output(Y3, 1)
else:
    IO.output(PULSE, 0)

for i in PULSE:
    LED = IO.PWM(i, 100)
    LED.start(0)

while cycle > 0:
    cycle -= 1
    LED.ChangeDutyCycle(random.randint(0, 100))
    time.sleep(1)
else:
    IO.output(PULSE, 0)
