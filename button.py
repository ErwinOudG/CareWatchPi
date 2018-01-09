# button.py
import urllib2
import RPi.GPIO as GPIO
from time import sleep
import requests
import smbus
import time

try:
   import RPi.GPIO as GPIO
except RuntimeError:
   print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
ledpin=4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 20   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
# LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
def main():
  # Main program block
  button_23_pressed = False
  button_24_pressed = False

  # Initialise display
  lcd_init()
  while True:

    if GPIO.input(23) is 0 and not button_23_pressed:
        LCD_BACKLIGHT  = 0x08  # On
        lcd_string("Fall detected",LCD_LINE_1)
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
        LCD_BACKLIGHT  = 0x08  # On
        lcd_string("Alarm Button Pressed",LCD_LINE_1)
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
if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)

LCD_BACKLIGHT = 0x00  # Off
GPIO.cleanup()
