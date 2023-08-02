import time
from adafruit_servokit import ServoKit

# Initialize the servo driver HAT
kit = ServoKit(channels=16)

# Specify the channels for your servo motors
servo_channels = [0, 1, 2, 3]  # Adjust this based on your setup


# Function to set servo angles
def set_servo_angle(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1)


# Function to stop the servo motor
def stop_servo(channel):
    kit.servo[channel].angle = None


try:
    # Set servo motors to neutral position (90 degrees)
    for channel in servo_channels:
        set_servo_angle(channel, 90)

    # Keep the servos in the neutral position for 15 seconds
    time.sleep(15)

    # Stop the servo motors
    for channel in servo_channels:
        stop_servo(channel)

finally:
    # Reset servo positions before exiting
    for channel in servo_channels:
        stop_servo(channel)
