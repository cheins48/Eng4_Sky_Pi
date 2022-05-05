#taken from Harriet Novaks repository.
import time
import board
import adafruit_mpl3115a2 # barometer library
import pwmio
from adafruit_motor import servo
import busio
from gpiozero import Servo
import RPi.GPIO as GPIO
import pigpio
#from micro:bit import *

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D18, duty_cycle=2 ** 15, frequency=50)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
#p = GPIO.PWM(18, 100)
#myGPIO = 18 # servo on pin 18

# fixes servo range to be full 180 degrees
# tutorial: https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000

#servo = Servo(GPIO, min_pulse_width = minPW, max_pulse_width = maxPW)
my_servo=Servo


while True:
	my_servo.angle = 180
	time.sleep(5)

	my_servo.angle = 0
	time.sleep(5)
