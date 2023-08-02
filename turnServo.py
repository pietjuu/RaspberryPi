# Libraries

from adafruit_servokit import ServoKit
from time import sleep, time

# Initialize the servo driver HAT
kit = ServoKit(channels=16)

# Specify the channels for your servo motors
servo_channels = [0, 1, 2, 3]


# Set the servo motors to their initial position
def set_servo_angle(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1)


try:
    # Rotate the servo motors
    for channel in servo_channels:
        set_servo_angle(channel, 0)  # Rotate to 0 degrees
        set_servo_angle(channel, 90)  # Rotate to 90 degrees
        set_servo_angle(channel, 180)  # Rotate to 180 degrees

except KeyboardInterrupt:
    # Reset servo positions to 90 degrees before exiting
    for channel in servo_channels:
        set_servo_angle(channel, 90)