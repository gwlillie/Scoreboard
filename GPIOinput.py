#doesn't work bc rpi.gpio is amde for older pis. rpi5 has new hardware

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
inPin = 40
GPIO.setup(inPin,GPIO.IN)

try:
    while True:
        readVal=GPIO.input(inPin)
        print(readVal)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
