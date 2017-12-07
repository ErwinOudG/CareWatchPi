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
button_2_pressed = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
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
    if GPIO.input(24) is 0 and not button_2_pressed:                            # Zorgt dat er een bericht met id 3 naar de database gaat
        # print("Button pressed")
        button_2_pressed = True
        sleep(0.1)
        try:
            # print("Wait")
            url='https://carew.oudgenoeg.nl/php/post.php'                       # Url naar de database
            data = {'id': 3, 'datatype': 'button', 'datavalue': 1}              # Id 3, er komt dus in de database button te staan
            r = requests.post(url,data=data)                                    # Post wat onder data staat naar de database
            r.close()                                                           # Sluit de connectie naar de database
        except Exceptions as e:
            print(e)
            print("No data found")                                              # Als er dus niks naar de database gestuurd kan worden, post hij dit op scherm
    if GPIO.input(24) is 1 and button_2_pressed:
        button_2_pressed = False
    sleep (0.01)
GPIO.cleanup()
