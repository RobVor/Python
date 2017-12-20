#!/usr/env/bin python3
#
# LCD.py - A program that prints characters as if it was an LCD display.

import os, sys, logging, time

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
#logging.disable(logging.DEBUG)

#Variables and Constants
logging.debug('Initializing Variables.')

#Classes (And exceptions)
logging.debug('Initializing custom Classes.')

#Functions
logging.debug('Initializing custom Functions.')

def GRID(SIZE):
    logging.debug('Standard LCD grid block.')
    HBAR = [" ","-"," "]
    VBAR = ["|"," ","|"]
    for i in range(SIZE):
        HBAR.insert(1, HBAR[1])
        VBAR.insert(1, VBAR[1])
    for n in range(5):
        if n == 0:
            print("".join(HBAR) * 10)
        elif n == 2:
            print("".join(HBAR) * 10)
        elif n == 4:
            print("".join(HBAR) * 10)
        else:
            if SIZE >= 1:
                for u in range((SIZE + 1)):
                    print("".join(VBAR) * 10)
            else:
                print("".join(VBAR) * 10)

def ONE(SIZE):
    logging.debug('Printing 1')
    HBAR = [" "," "," "]
    VBAR = [" "," ","|"]
    for i in range(SIZE):
        HBAR.insert(1, HBAR[1])
        VBAR.insert(1, VBAR[1])
    for n in range(5):
        if n == 0:
            print("".join(HBAR) * 10)
        elif n == 2:
            print("".join(HBAR) * 10)
        elif n == 4:
            print("".join(HBAR) * 10)
        else:
            if SIZE >= 1:
                for u in range((SIZE + 1)):
                    print("".join(VBAR) * 10)
            else:
                print("".join(VBAR) * 10)
    
def TWO(SIZE):
    logging.debug('Printing 2')
    HBAR = [" ","-"," "]
    VBAR = ["|"," ","|"]
    for i in range(SIZE):
        HBAR.insert(1, HBAR[1])
        VBAR.insert(1, VBAR[1])
    for n in range(5):
        if n == 0:
            print("".join(HBAR) * 10)
        elif n == 2:
            print("".join(HBAR) * 10)
        elif n == 4:
            print("".join(HBAR) * 10)
        else:
            if SIZE >= 1:
                for u in range((SIZE + 1)):
                    print("".join(VBAR) * 10)
            else:
                print("".join(VBAR) * 10)
                
def THREE(SIZE):
    logging.debug('Printing 3')
def FOUR(SIZE):
    logging.debug('Printing 4')
def FIVE(SIZE):
    logging.debug('Printing 5')
def SIX(SIZE):
    logging.debug('Printing 6')
def SEVEN(SIZE):
    logging.debug('Printing 7')
def EIGHT(SIZE):
    logging.debug('Printing 8')
def NINE(SIZE):
    logging.debug('Printing 9')
def ZERO(SIZE):
    logging.debug('Printing 0')

#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

os.system('clear')
GRID(3)
time.sleep(2)
os.system('clear')
ONE(3)
time.sleep(2)
os.system('clear')
TWO(3)

print('This program will print input as though it where an LCD display')

#End
logging.debug('Program end and cleanup.')
