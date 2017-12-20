#!/usr/bin/env python3
#
# collatz.py - A program to illustrate the Collatz sequence.

import os, sys, logging

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
#logging.disable(logging.DEBUG)

#Variables and Constants
logging.debug('Initializing Variables.')
CYCLE1 = 0
CYCLE2 = 0
CYCLE3 = 0
CYCLE4 = 0
IN1 = None
IN2 = None
IN3 = None
IN4 = None
VAL = None

#Classes
logging.debug('Initializing custom Classes.')

class QBreak(Exception):
    """Called when the 'q' value is passed to the system. This initiates a call to quit."""

#Functions
logging.debug('Initializing custom Functions.')

def CAPTURE():
    while True:
        try:
            NUMBERS = input('Please type in 4 numeric values seperated by a space or press q to quit: ').split()
            logging.debug('Capturing input.')
            logging.debug('Input is: ' + str(NUMBERS))
            if 'q' in NUMBERS:
                raise QBreak
            else:
                for n in NUMBERS:
                    if int(n) in range(1000000):
                        logging.debug('Matched to number.')
                return NUMBERS
        except QBreak:
            logging.debug('Quit selected. Quitting...')
            print('Please only use positive numeric values.')
            break

def COLLATZ(NUMBERS):
    for n in range(4):
        NUMBERS[n] = int(NUMBERS[n])
        logging.debug('Number conversions done.')
        
#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

CAPTURE()

#End
logging.debug('Program end and cleanup.')
