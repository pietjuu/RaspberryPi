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


# Set the speed of the continuous rotation servo
def setServoAngle(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1)


# Function to stop the servo motor
def stopServo(channel):
    kit.servo[channel].angle = None
try:

    # Start the first motor
    setServoAngle(servo_channels[0], 90)
    time.sleep(5)  # Run for 5 seconds
    stopServo(servo_channels[0])

    # Wait 5 seconds
    time.sleep(5)

    # Start the second motor
    setServoAngle(servo_channels[1], 90)
    time.sleep(5)  # Run for 5 seconds
    stopServo(servo_channels[1])

    # Wait 5 seconds
    time.sleep(5)

    # Start the third motor
    setServoAngle(servo_channels[2], 90)
    time.sleep(5)  # Run for 5 seconds
    stopServo(servo_channels[2])

    # Wait 5 seconds
    time.sleep(5)

    # Start the fourth motor
    setServoAngle(servo_channels[3], 90)
    time.sleep(5)  # Run for 5 seconds
    stopServo(servo_channels[3])

finally:
    # Stop all motors before exiting
    for channel in servo_channels:
        stopServo(channel)
