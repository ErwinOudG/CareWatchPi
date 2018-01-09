# button.py
import urllib2
import RPi.GPIO as GPIO
from time import sleep
import requests
try:
   import RPi.GPIO as GPIO
except RuntimeError:
   print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
ledpin=4
button_23_pressed = False
button_24_pressed = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    # if (GPIO.input(23) == 1):
    #     try:
    #            print ("Getting URL")
    #            response = urllib2.urlopenn("http://python.org")
    #            html = response.read()
    #            print "help"
    #     except:
    #         print ("Failed to fetch")
    if GPIO.input(23) is 0 and not button_23_pressed:
        print("Button pressed")
        button_23_pressed = True
        sleep(0.1)
        try:
            print("Wait, connecting to database")
            url='https://carew.oudgenoeg.nl/php/post.php'
            data = {'id': 3, 'datatype': 'fallen', 'datavalue': 1}
            r = requests.post(url,data=data)
            r.close()
            print data
        except Exception as e:
            print(e)
            print("No data found")
    if GPIO.input(23) is 1 and button_23_pressed:
        button_23_pressed = False
    sleep (0.01)
    if GPIO.input(24) is 0 and not button_24_pressed:
        print("Button pressed")
        button_24_pressed = True
        sleep(0.1)
        try:
            print("Wait, connecting to database")
            url='https://carew.oudgenoeg.nl/php/post.php'
            data = {'id': 3, 'datatype': 'button', 'datavalue': 1}
            r = requests.post(url,data=data)
            r.close()
            print data
        except Exception as e:
            print(e)
            print("No data found")
    if GPIO.input(24) is 1 and button_24_pressed:
        button_24_pressed = False
    sleep (0.01)
GPIO.cleanup()
