import time
from adafruit_servokit import ServoKit

# Initialize the servo driver HAT
kit = ServoKit(channels=16)

# Specify the channels for your servo motors
servo_channels = [0, 1, 2, 3]  # Adjust this based on your setup


# Function to set servo angles
def setServoAngle(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1)


# Function to stop the servo motor
def stopServo(channel):
    kit.servo[channel].angle = None


def rotateServo():
    try:
        # Set servo motors to neutral position (90 degrees)
        for channel in servo_channels:
            setServoAngle(channel, 90)

        # Keep the servos in the neutral position for 15 seconds
        time.sleep(15)

        # Stop the servo motors
        for channel in servo_channels:
            stopServo(channel)

    finally:
        # Reset servo positions before exiting
        for channel in servo_channels:
            stopServo(channel)


rotateServo()