#!/usr/bin/env python3
#
# banner.py - Script to take an argument or clipboard content or normal text and convert it to a simple banner.
 
import os, sys, logging

banner_text = None
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Program Start')

if len(sys.argv) < 2:
    logging.debug('No arguments, moving to user input.')
    print("Skipping system arguments and using manual input.")
    print("Please type in the text or name you want in a banner.")
    banner_text = input()
else:
    banner_text = ""
    for arg in sys.argv:
        if arg == sys.argv[0]:
            next
        else:
            arg.strip()
            banner_text = banner_text + " " + arg

logging.debug('Argument or input available, starting routine.')

def banner_me(text):
    logging.debug('Building banner.')
    if text.startswith(" "):
        text = text[1:]
    newStr = '*' * (len(text) + 4)
    print(newStr)
    print()
    print('* ' + text + ' *')
    print()
    print(newStr)
    logging.debug('Banner done!')

banner_me(banner_text)
