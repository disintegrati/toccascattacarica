import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonPin,GPIO.OUT)
status = GPIO.input(buttonPin)
try: 
  while True:
    print(status)
  #assuming the script to call is long enough we can ignore bouncing
    if (status):
    #this is the script that will be called (as root)
    #os.system("python /home/pi/start.py")
      print("PRESSD")
except KeyboardInterrupt:
    GPIO.cleanup()
