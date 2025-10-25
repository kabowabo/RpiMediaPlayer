import RPi.GPIO as GPIO
import time

BL_PIN = 18  # Replace with your actual GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(BL_PIN, GPIO.OUT)

GPIO.output(BL_PIN, GPIO.LOW)  # Turn off backlight
# GPIO.output(BL_PIN, GPIO.HIGH)  # To turn it back on

