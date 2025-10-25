import RPi.GPIO as GPIO
import time

BL_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BL_PIN, GPIO.OUT)

GPIO.output(BL_PIN, GPIO.LOW)

