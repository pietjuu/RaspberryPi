'''
when button is pressed, light goes on for 20 seconds
after 5 seconds the first motor starts, then after 10 seconds the second motor starts,
then after 15 seconds the third motor starts, then after 20 seconds the fourth motor starts
'''

# Libraries
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

# Set warnings off
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set pins for button and LED
Button = 23
Led = 24

# Set start state
GPIO.setup(Button, GPIO.IN)
GPIO.setup(Led, GPIO.OUT)

# Initialize the servo driver HAT
kit = ServoKit(channels=16)

# Specify the channels for your servos
servo_channels = [0, 1, 2, 3]  # Adjust this based on your setup


# Function to set servo angles and directions
def setServoAngle(channel, angle, direction):
    if direction == "forward":
        kit.servo[channel].angle = angle
    elif direction == "backward":
        kit.servo[channel].angle = 180 - angle  # Adjusted angle for backward movement
    time.sleep(0.1)


# Function to rotate the servo at a specific speed
def setServoSpeed(channel, speed, direction):
    if direction == "forward":
        kit.servo[channel].angle += speed
    elif direction == "backward":
        kit.servo[channel].angle -= speed
    time.sleep(0.1)


# Function to stop the servo motor
def stopServo(channel):
    kit.servo[channel].angle = None

    try:
        # Start the first motor forward
        setServoAngle(servo_channels[0], 90, "forward")
        time.sleep(5)  # Run for 5 seconds

        # Rotate the first motor backward
        setServoSpeed(servo_channels[0], 1, "backward")
        time.sleep(2)  # Run for 2 seconds
        stopServo(servo_channels[0])

    finally:
        # Stop all motors before exiting
        for channel in servo_channels:
            stopServo(channel)
