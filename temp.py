# temp.py
import urllib2
import random
from time import sleep
import requests
while True:
    sleep(60)
    rndtemp = random.uniform(240, 340) / 10                                     # Genereert een random nummer die een tempratuur simuleert en dat naar de database stuurt 
    try:
        # print("Wait")
        url='https://carew.oudgenoeg.nl/php/post.php'                           #Url waar de tempratuur heen gaat
        data = {'id': 3, 'datatype': 'temperature', 'datavalue': rndtemp}
        r = requests.post(url,data=data)
        r.close()
    except Exceptions as e:
        print(e)
        print("No data found")
GPIO.cleanup()
