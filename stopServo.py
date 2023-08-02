import time
from adafruit_servokit import ServoKit

# Initialize the servo driver HAT
kit = ServoKit(channels=16)

# Specify the channels for your servo motors
servo_channels = [0, 1, 2, 3]  # Adjust this based on your setup

# Function to stop the servo motor
def stop_servo(channel):
    kit.servo[channel].angle = None

try:
    # Stop the servo motors
    for channel in servo_channels:
        stop_servo(channel)

    # Keep the servos stopped for a few seconds
    time.sleep(5)

finally:
    # Reset servo positions before exiting
    for channel in servo_channels:
        stop_servo(channel)
