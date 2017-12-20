import os, sys, logging, sqlite3, time
import RPi.GPIO as GPIO

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
#logging.disable(logging.DEBUG) """ remember to use logging.exception for traceback and line numbers """

#Database builder
logging.debug('Initializing Databases and connections.')

#Variables and Constants
logging.debug('Initializing Variables.')

CLOCK = 26    #P11
LATCH = 19    #P12
INPUT = 13    #P14
SHOW = 6      #P13
PINS = [CLOCK, LATCH, INPUT, SHOW]

#Classes (And exceptions)
logging.debug('Initializing custom Classes.')

class NoInput():
    pass

#Functions
logging.debug('Initializing custom Functions.')

def CLSC():
    os.system("cls" if os.name == "nt" else "clear")

def PORTS():
    logging.debug('Setting up ports.')
    GPIO.setmode(GPIO.BCM)
    for i in PINS:
        GPIO.setup(i, GPIO.OUT)

def CLOCK_PULSE(q):
    if q < 1:
        q = 1
    for x in range(0,q):
        GPIO.output(CLOCK, 0)
        #time.sleep(0.01)
        GPIO.output(CLOCK, 1)
    return

def LATCH_IN():
    GPIO.output(LATCH, 0)
    #time.sleep(0.01)
    GPIO.output(LATCH, 1)
    return

def TESTBLOCK():
    '''
    for x in range(0,8):
        GPIO.output(INPUT, 1)
        CLOCK_PULSE()
        GPIO.output(INPUT, 0)
        CLOCK_PULSE()
    LATCH_IN()
    for x in range(0,8):
        GPIO.output(INPUT, 0)
        CLOCK_PULSE()
        GPIO.output(INPUT, 1)
        CLOCK_PULSE()
    LATCH_IN()
    '''
    '''
    GPIO.output(INPUT, 1)
    for x in range(0,8):
        CLOCK_PULSE()
        LATCH_IN()
        time.sleep(0.1)
    GPIO.output(INPUT, 0)
    for y in range(0,8):
        CLOCK_PULSE()
        LATCH_IN()
        time.sleep(0.1)
    '''
    GPIO.output(SHOW, 0)
    GPIO.output(INPUT, 1)
    for x in range(0,8):
        CLOCK_PULSE(4)
        LATCH_IN()
        time.sleep(0.2)
    GPIO.output(INPUT, 0)
    for y in range(0,8):
        CLOCK_PULSE(2)
        LATCH_IN()
        time.sleep(0.2)
    GPIO.output(SHOW, 1)
    return

#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

PORTS()
x = 0
while x < 10:
    x += 1
    TESTBLOCK()

#End
logging.debug('Program end and cleanup.')
GPIO.cleanup()
