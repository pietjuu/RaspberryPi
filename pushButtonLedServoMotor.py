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

# Specify the channels for your servo motors
servo_channels = [0, 1, 2, 3]  # Adjust this based on your setup


def setServoAngle(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1)


# Set the speed of the continuous rotation servo
def set_servo_speed(channel, speed):
    kit.continuous_servo[channel].throttle = speed


# Stop the continuous rotation servo
def stop_servo(channel):
    for channel in servo_channels:
        setServoAngle(channel, 90)

    print("stop_servo")


def rotateServo():
    try:
        for servo_channel in servo_channels:
            # Rotate the servo at full speed clockwise
            set_servo_speed(servo_channel, 1)
            time.sleep(2)  # Run for 2 seconds

        time.sleep(1)  # Pause for 1 second

        for servo_channel in servo_channels:
            # Rotate the servo at full speed counterclockwise
            set_servo_speed(servo_channel, -1)
            time.sleep(2)  # Run for 2 seconds

        # Stop the servo motors
        for channel in servo_channels:
            stop_servo(channel)

    finally:
        # Stop the servo before exiting
        for channel in servo_channels:
            stop_servo(channel)


rotateServo()
