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
CYCLE = 0
VAL = None

#Classes
logging.debug('Initializing custom Classes.')

class QBreak(Exception):
    """Called when the 'q' value is passed to the system. This initiates a call to quit."""

#Functions
logging.debug('Initializing custom Functions.')

def CAPTURE():
    NUMBERS = input('Please type in 4 numbers seperated by a space: ').split()
    return NUMBERS

def COLLATZ(NUMBERS):
    for n in range(4):
        NUMBERS[n] = int(NUMBERS[n])
        logging.debug('Number conversions done.')
        
#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

try:
    while True:
        VAL = CAPTURE()
        COLLATZ(VAL)
except ValueError:
    logging.debug('Incorrect value.')
except IndexError:
    logging.debug('Not enough values provided or too many.')

#End
logging.debug('Program end and cleanup.')
