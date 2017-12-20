#!/usr/bin/python3
#
# Setting up new wiring. Testing leds Red, Yellow, Green.

import gpio as IO
import paho.mqtt.client as mqtt
import pymysql as MYSQL
import time, os, sys, random

CLK = float(input("What is the clock timing you want to use? "))

def Run(CLK):
    for i in LEDS:
        IO.output(i, 1)
        time.sleep(CLK)
    for i in LEDS:
        IO.output(i, 0)
        time.sleep(CLK)

def RevRun(CLK):
    for i in reversed(LEDS):
        IO.output(i, 1)
        time.sleep(CLK)
    for i in reversed(LEDS):
        IO.output(i, 0)
        time.sleep(CLK)

def RunEnd():
    for i in LEDS:
        IO.output(i, 0)
        time.sleep(0.001)
        IO.cleanup(i)

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
Trigger = 14


LEDS = [26, 21, 20, 13, 6, 12, 7, 8, 11 ]

for i in LEDS:
    IO.setup(i, IO.OUT)
try:
    while True:
        IO.setup(Trigger, IO.IN)
        print(IO.read(Trigger))
except KeyboardInterrupt:
    RunEnd()
exit()
