# Libraries

from adafruit_servokit import ServoKit
import time

# Initialize the servo driver HAT
kit = ServoKit(channels=16)

# Specify the channels for your servo motors
servo_channels = [0, 1, 2, 3]


# Set the servo motors to their initial position
def set_servo_angle(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1)


# Reset servo positions to neutral before exiting
try:
    # Set servo motors to neutral position (90 degrees)
    for channel in servo_channels:
        set_servo_angle(channel, 90)

    # Keep the servos in the neutral position for a few seconds
    time.sleep(5)

finally:
    # Reset servo positions to 90 degrees before exiting
    for channel in servo_channels:
        set_servo_angle(channel, 90)