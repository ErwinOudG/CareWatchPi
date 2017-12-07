# led1sec.py
import RPi.GPIO as GPIO
from time import sleep
from time import sleep
import requests
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
        sleep(0.5)
        try:
            # print("Wait")
            url='https://carew.oudgenoeg.nl/php/request.php'
            data = {'id': 3, 'datatype': 'button', 'datavalue': 1}
            r = requests.Request(url,data=data)
            respo = urllib2.urlopen(r)
            drespo = respo.read()
            print drespo
            r.close()
        except Exceptions as e:
            print(e)
            print("No data found")
GPIO.cleanup()
