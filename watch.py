# watch.py
import urllib2
import RPi.GPIO as GPIO
from time import sleep
import requests
import datetime
try:
   import RPi.GPIO as GPIO
except RuntimeError:
   print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
ledpin=4
timerbegin = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    timerdif = (datetime.datetime.now() - timerbegin).total_seconds() / 60.0
    print timerdif
    if (timerdif >= 1):
        timerbegin = datetime.datetime.now()
        try:
            print("Wait")
            url='http://carew.oudgenoeg.nl/php/post.php'
            data = {'id':3}
            r = requests.post(url,data=data)
        except Exceptions as e:
            print(e)
            print("No data found")
    if (GPIO.input(23) == 1):
        try:
               print ("Getting URL")
               respomse = urllib2.urlopenn("http://python.org")
               html = response.read()
               print "help"
        except:
            print ("Failed to fetch")
    if GPIO.input(24) is 0 and not button_2_pressed:
        button_2_pressed = True
        sleep(0.1)
        try:
            print("Wait")
            url='http://carew.oudgenoeg.nl/php/post.php'
            data = {'id':1}
            r = requests.post(url,data=data)
        except Exceptions as e:
            print(e)
            print("No data found")
    if GPIO.input(24) is 1 and button_2_pressed:
        button_2_pressed = False
    sleep (0.01)
GPIO.cleanup()
