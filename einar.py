import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22,GPIO.IN)



if GPIO.input(22, True):
    GPIO.output(4, True)
    time.sleep(3)
    GPIO.output(4, False)
