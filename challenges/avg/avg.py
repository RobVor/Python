#!/usr/env/bin python3
# avg.py - An application that calculates mean, mode and standard averages from user supplied values.

import time, random, sys, os, logging, re

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
logging.disable(logging.DEBUG)

#Variables
logging.debug('Initializing Variables.')
AVERAGE_VALUES = []
MEAN_ANSWER = None
MODE = None
MEDIAN = None

#Classes
logging.debug('Initializing custom Classes.')

#Functions
logging.debug('Initializing custom Functions.')

def MEAN(LST):
    logging.debug('Calculating mean average.')
    MEAN_ANSWER = 0
    for i in LST:
        logging.debug('MEAN: ' + str(MEAN_ANSWER))
        MEAN_ANSWER += i
    MEAN_ANSWER = MEAN_ANSWER / len(LST)
    logging.debug('Final MEAN: ' + str(MEAN_ANSWER))
    return MEAN_ANSWER

def MODE(LST):
    logging.debug('Calculating mode average')
    MODE = max(LST, key=LST.count)
    logging.debug('MODE:' + str(MODE))
    return MODE

def MEDIAN(LST):
    logging.debug('Getting median.')
    SORT = sorted(LST)
    ODD = None
    EVEN = None
    if len(LST) % 2 == 0:
        EVEN = (SORT[(int(len(LST) / 2) - 1)] + SORT[(int(len(LST) / 2))]) / 2
        logging.debug('Even is: ' + str(EVEN))
        return EVEN
    else:
        ODD = SORT[(int(len(LST) / 2))]
        logging.debug('Odd is: ' + str(ODD))
        return ODD
#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')
while True:
    try:
        IN = input('Please type in at least 2 numeric values seperated by a space: ').split()
        logging.debug('Input captured as: ' + str(IN))
        for i in IN:
            AVERAGE_VALUES.append(int(i))
        if not AVERAGE_VALUES:
            logging.debug('Blank values are not allowed.')
            continue
        else:
            logging.debug('AVERAGE_VALUES are captured as: ' + str(AVERAGE_VALUES))
            MEAN(AVERAGE_VALUES)
            MODE(AVERAGE_VALUES)
            MEDIAN(AVERAGE_VALUES)
            print('Supplied list of values was: ' + str(AVERAGE_VALUES))
            print('The average is: ' + str(MEAN(AVERAGE_VALUES)))
            print('The mode is: ' + str(MODE(AVERAGE_VALUES)))
            print('The median is: ' + str(MEDIAN(AVERAGE_VALUES)))
            break
        break
    except KeyboardInterrupt:
        break

#End
logging.debug('Program end and cleanup.')
