# heartb.py
import urllib2
import random
from time import sleep
import requests
while True:
    sleep(300)
    rndbeat = random.randint(55, 90)                                            # Genereert een random nummer die een hartslag moet simuleren die dan naar de database gaat
    try:
        # print("Wait")
        url='https://carew.oudgenoeg.nl/php/post.php'                           # URL waar het nummer wordt naar gestuurd
        data = {'id': 3, 'datatype': 'heartbeat', 'datavalue': rndbeat}
        r = requests.post(url,data=data)
        r.close()
    except Exceptions as e:
        print(e)
        print("No data found")
GPIO.cleanup()
