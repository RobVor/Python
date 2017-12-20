#!/usr/bin/env python3
#
# mmind.py - Mastermind guessing game

import RPi.GPIO as IO
import time, random, sys, os, logging, re

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
logging.disable(logging.DEBUG)

#Variables
logging.debug('Initializing Variables.')

GO = 21
R1 = 26
R2 = 20
R3 = 19
R4 = 16
Y1 = 13
Y2 = 6
Y3 = 12
Y4 = 5
LEDS = [21, 26, 20, 19, 16, 13, 6, 12, 5]
count = 0
S0 = 0
S1 = 0
S2 = 0
S3 = 0
SERVER = None
GUESS = None
G0 = 0
G1 = 0
G2 = 0
G3 = 0

#Classes
logging.debug('Initializing custom Classes.')

#Functions
logging.debug('Initializing custom Functions.')

def LED_RUN(LEDS):
    for i in LEDS:
        IO.output(i, 1)
        time.sleep(0.05)
        IO.output(i, 0)
        time.sleep(0.05)
    for i in LEDS:
        IO.output(i, 1)
        time.sleep(0.02)
    for i in LEDS:
        IO.output(i, 0)
        time.sleep(0.02)
    for i in reversed(LEDS):
        IO.output(i, 1)
        time.sleep(0.02)
    for i in reversed(LEDS):
        IO.output(i, 0)
        time.sleep(0.02)

def SERVER_GUESS():
    S0 = random.randint(0, 9)
    S1 = random.randint(0, 9)
    S2 = random.randint(0, 9)
    S3 = random.randint(0, 9)
    logging.debug('Sequence is: ' + str(S0) + str(S1) + str(S2) + str(S3))
    SERVER = str(S0) + str(S1) + str(S2) + str(S3)
    return str(SERVER)

def PLAYER_GUESS():
    logging.debug('Getting player guessed values...')
    GUESS = 0
    num = re.compile('^[0-9]{4}$')
    while True:
        GUESS = input('Guess 4 numbers: ')
        if num.match(GUESS) is not None:
            return GUESS
        else:
            logging.debug('Wrong value.')
            print('Sorry, please only use 4 numbers.')

def COMPARE(HOST, GUEST):
    logging.debug("Host: " + HOST)
    logging.debug("GUEST: " + GUEST)
    REDS = [26, 20, 19, 16]
    YELLOWS = [13, 6, 12, 5]
    for i in range(0, 4):
        if GUEST[i] == HOST[i]:
            IO.output(YELLOWS[i], 1)
            IO.output(REDS[i], 0)
        else:
            IO.output(REDS[i], 1)
            IO.output(YELLOWS[i], 0)

#GPIO
logging.debug('Setting up I/O pins.')

IO.setmode(IO.BCM)
for i in LEDS:
    IO.setup(i, IO.OUT)

#Main
logging.debug('Program main start.')

try:
    logging.debug('Setting up game.')
    SERVER = SERVER_GUESS()
    logging.debug('Host guessing complete. Numbers are: ' +  str(SERVER))
    logging.debug('Testing led notification.')
    LED_RUN(LEDS)
    logging.debug('Start guessing.')
    IO.output(GO, 1)
    while True:
        count += 1
        os.system('clear')
        GUESS = PLAYER_GUESS()
        logging.debug('Guess successfully captured.')
        COMPARE(SERVER, GUESS)
        if SERVER == GUESS:
            break
        else:
            print("Try again.")
            continue
except KeyboardInterrupt:
    logging.debug('Sequence end.')

#End

os.system('clear')
print("We have a Winner!!!! And it only took " + str(count) + " turns!")
logging.debug("Winner!")
time.sleep(0.02)
for i in range(0, 2):
    LED_RUN(LEDS)

logging.debug('Program end and cleanup.')

IO.cleanup()
sys.exit()
