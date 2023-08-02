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
def set_servo_speed(channel, speed):
    kit.continuous_servo[channel].throttle = speed


# Stop both continuous rotation and standard servos
def stop_servo(channel):
    kit.continuous_servo[channel].throttle = 0
    kit.servo[channel].angle = None


try:
    # Turn on LED for 20 seconds when button is pressed
    if GPIO.input(Button) == GPIO.HIGH:
        GPIO.output(Led, GPIO.HIGH)
        time.sleep(20)
        GPIO.output(Led, GPIO.LOW)

    # Wait 5 seconds
    time.sleep(5)

    # Start the first motor
    set_servo_speed(servo_channels[0], 1)
    time.sleep(5)  # Run for 5 seconds
    stop_servo(servo_channels[0])

    # Wait 5 seconds
    time.sleep(5)

    # Start the second motor
    set_servo_speed(servo_channels[1], 1)
    time.sleep(5)  # Run for 5 seconds
    stop_servo(servo_channels[1])

    # Wait 5 seconds
    time.sleep(5)

    # Start the third motor
    set_servo_speed(servo_channels[2], 1)
    time.sleep(5)  # Run for 5 seconds
    stop_servo(servo_channels[2])

    # Wait 5 seconds
    time.sleep(5)

    # Start the fourth motor
    set_servo_speed(servo_channels[3], 1)
    time.sleep(5)  # Run for 5 seconds
    stop_servo(servo_channels[3])

finally:
    # Stop all motors before exiting
    for channel in servo_channels:
        stop_servo(channel)
