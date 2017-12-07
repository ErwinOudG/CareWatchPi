# led1sec.py
import RPi.GPIO as GPIO
from time import sleep
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
ledpin=4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    if (GPIO.input(23) == 1):
        print "Button 1 pressed"
        GPIO.output(ledpin, 1)
        sleep(0.1)
        GPIO.output(ledpin, 0)
        sleep(0.1)
        GPIO.output(ledpin, 1)
        sleep(0.1)
        GPIO.output(ledpin, 0)
        sleep(0.1)
        GPIO.output(ledpin, 1)
        sleep(0.1)
        GPIO.output(ledpin, 0)
        sleep(0.1)
        GPIO.output(ledpin, 1)
        sleep(1)
        GPIO.output(ledpin, 0)
    if(GPIO.input(24) == 0):
        print "Button 2 pressed"
        GPIO.output(ledpin, 1)
        sleep(1)
        GPIO.output(ledpin, 0)
        sleep(0.1)
        GPIO.output(ledpin, 1)
        sleep(0.1)
        GPIO.output(ledpin, 0)
        sleep(0.1)
        GPIO.output(ledpin, 1)
        sleep(0.1)
        GPIO.output(ledpin, 0)
        sleep(0.1)
        GPIO.output(ledpin, 1)
        sleep(0.1)
        GPIO.output(ledpin, 0)
GPIO.cleanup()
