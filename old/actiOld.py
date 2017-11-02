import RPi.GPIO as GPIO
import time
import os
prev_input = 0
#adjust for where your switch is connected
buttonPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
  input = GPIO.input(buttonPin)
  #assuming the script to call is long enough we can ignore bouncing
  if ((not prev_input) and input):
    #this is the script that will be called (as root)
    os.system("sh /home/pi/Desktop/uplpyt/scatta.sh")
    print("scatto foto!!!")
  prev_input = input
  time.sleep(1)
