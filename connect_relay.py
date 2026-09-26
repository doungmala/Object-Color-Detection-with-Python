import RPi.GPIO as GPIO
import time
from time import sleep

relay_ch = 4
# RED ON THEN OFF
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_ch, GPIO.OUT)
GPIO.output(relay_ch, GPIO.LOW)
time.sleep(1)
GPIO.output(relay_ch, GPIO.HIGH)
GPIO.cleanup()
