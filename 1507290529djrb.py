
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(22,GPIO.IN)

GPIO.output(25, False)

tminutes = 120
# tminutes '=value' to be replaced with parsed int value from xml or txt file
tseconds = 60*tminutes

while True:

        x = 0
        y = 0

        while GPIO.input(22):
                        time.sleep(0.25)
                        x = x+0.25
                        while x == 2: 
                                GPIO.output(25,1)
                                time.sleep(0.25)
                                y=y+0.25
                                if GPIO.input(22):
                                        y = 0
                                elif y==tseconds:
                                        GPIO.output(25,0)
                                        x = 0
                                        y = 0
                                        break


