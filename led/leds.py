#!
#
# Testing GPIO LED control through GPIO ports and 470 ohm resistors.

import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)

for i in 17, 18, 27:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 1)
    time.sleep(0.5)
    GPIO.output(i, 0)

GPIO.cleanup()
exit()
