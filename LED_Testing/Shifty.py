#!/usr/bin/python3_sudo.sh
import RPi.GPIO as GPIO
import time
import random as rand

SDI = 10
RCLK =9
SRCLK = 11

# ===============   LED Mode Defne ================
#	You can define yourself, in binay, and convert it to Hex
#	8 bits a group, 0 means off, 1 means on
#	like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#	and convert to 0x55.

LED0 = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]  # original mode
LED1 = [0x01, 0x03, 0x07, 0x0f, 0x1f, 0x3f, 0x7f, 0xff]  # blink mode 1
LED2 = [0x01, 0x05, 0x15, 0x55, 0xb5, 0xf5, 0xfb, 0xff]  # blink mode 2
LED3 = [0x02, 0x03, 0x0b, 0x0f, 0x2f, 0x3f, 0xbf, 0xff]  # blink mode 3
LED4 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
LED5 = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x02, 0x03, 0x0b, 0x0f, 0x2f, 0x3f, 0xbf, 0xff]
LED6 = [0x81, 0x42, 0x24, 0x18, 0x24, 0x42, 0x81, 0x00, 0xa5, 0x00, 0xa5, 0x00, 0x42, 0x00, 0x42, 0x00, 0x18, 0x00, 0x18, 0x00, 0xff, 0x00, 0xff, 0x00]
LED7 = [0x81, 0x42, 0x24, 0x18, 0x81, 0xc3, 0xe7, 0xff]
LED8 = [0x81, 0x42, 0x24, 0x18, 0xff, 0xe7, 0xc3, 0x81]
ALL_ON = [0xff, 0xff]
RESET = [0x00]
SEQ = []+LED0+LED1+LED2+LED3+LED4+LED5+LED6+ALL_ON
TEST_CHECK = [1,2,4,8,16,32,64,128,5,10,20,40,80,160]
TEST_CHECK2 = []
TEST_CHECK3 = [0, 510]

# =================================================

def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')


def setup():
    GPIO.setmode(GPIO.BCM)  # Number GPIOs by its physical location
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)


def hc595_in(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)


def hc595_out():
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)


def loop():
    WhichLeds = LED6  # Change Mode, modes from LED0 to LED3
    sleeptime = 0.15  # Change speed, lower value, faster speed
    while True:
        del TEST_CHECK2[:]
        for i in range(0, 9):
            TEST_CHECK2.append(rand.randrange(0x00, 0xff + 1))
        print(TEST_CHECK2)
        if WhichLeds == SEQ:
            for i in range(0, len(WhichLeds)):
                hc595_in(WhichLeds[i])
                hc595_out()
                time.sleep(sleeptime)
        else:
            for i in range(0, len(WhichLeds)):
                hc595_in(WhichLeds[i])
                hc595_out()
                time.sleep(sleeptime)

            for i in range(len(WhichLeds) - 1, -1, -1):
                hc595_in(WhichLeds[i])
                hc595_out()
                time.sleep(sleeptime)


def destroy():  # When program ending, the function is executed.
    hc595_in(RESET[0])
    hc595_out()
    GPIO.cleanup()


if __name__ == '__main__':  # Program starting from here
    print_msg()
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()