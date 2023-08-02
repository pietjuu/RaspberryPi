# Libraries
import RPI.GPIO as GPIO
from time import sleep

# Set warnings off
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set pins for button and LED
Button = 23
Led = 24

# Set start state
GPIO.setup(Button, GPIO.IN)
GPIO.setup(Led, GPIO.OUT)

# control the lights
while i < 10:
    if GPIO.input(Button) == GPIO.HIGH:
        GPIO.output(Led, GPIO.HIGH)
        sleep(1)
        GPIO.output(Led, GPIO.LOW)
        sleep(1)
        i: int = i + 1
    else:
        GPIO.output(Led, GPIO.LOW)

