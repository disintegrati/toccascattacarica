from time import sleep
from gpiozero import Button
import os
import RPi.GPIO as GPIO
button = Button(18)

while True: 
  try:
   button.wait_for_press()
   os.system("sh /home/pi/Desktop/uplpyt/scatta.sh")
   print("Scatto foto!")
   sleep(5)
  except KeyboardInterrupt:
   GPIO.cleanup()
   break
