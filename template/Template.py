import os, sys, logging, sqlite3

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
#logging.disable(logging.DEBUG) """ remember to use logging.exception for traceback and line numbers """

#Database builder
logging.debug('Initializing Databases and connections.')

#Variables and Constants
logging.debug('Initializing Variables.')

#Classes (And exceptions)
logging.debug('Initializing custom Classes.')

class NoInput():
    pass

#Functions
logging.debug('Initializing custom Functions.')

def CLSC():
    os.system("cls" if os.name == "nt" else "clear")

#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

#End
logging.debug('Program end and cleanup.')
