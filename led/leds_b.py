#!
#
# Testing GPIO LED control through GPIO ports and 470 ohm resistors.

import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)

for i in 17, 18, 27, 23, 22:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, 1)
    time.sleep(0.5)
    GPIO.output(i, 0)

print("System test done. Ready for some action...!")

GPIO.setup(2, GPIO.IN)

while 1:
    if GPIO.input(2):
        GPIO.output(18, 0)
    else:
        GPIO.output(18 ,1)

GPIO.cleanup()
exit()
