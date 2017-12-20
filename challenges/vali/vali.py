#!/usr/bin/env python3
#
# vali.py - An e-mail validator. Can accept e-mail address as argument.

import sys, os, logging

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
#logging.disable(logging.DEBUG)

#Variables
logging.debug('Initializing Variables.')

#Classes
logging.debug('Initializing custom Classes.')

#Functions
logging.debug('Initializing custom Functions.')

#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

if len(sys.argv) < 2:
    logging.debug('No arguments have been provided, moving on to user input.')
    EMAIL = input('Please type in an e-mail to validate: ')
else:
    logging.debug('Argument supplied.')
    EMAIL = None
    for ARG in sys.argv:
        if ARG == sys.argv[0]:
            next
        else:
            ARG.strip()
            EMAIL = ARG

logging.debug('Captured email as: ' + str(EMAIL))

if '@' in EMAIL:
    logging.debug('Email contains @.')
    logging.debug('Moving onto next check.')
else:
    logging.debug('Address probably not correct.')

#End
logging.debug('Program end and cleanup.')
