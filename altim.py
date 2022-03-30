#taken from Harriet Novaks repository.
import time
import board
import adafruit_mpl3115a2 # barometer library
import busio
from gpiozero import Servo
import RPi.GPIO as GPIO
import pigpio

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 100)
#myGPIO = 18 # servo on pin 18

# fixes servo range to be full 180 degrees
# tutorial: https://www.raspberrypi-spy.co.uk/2018/02/basic-servo-use-with-the-raspberry-pi/
correction = 0.45
maxPW = (2.0 + correction)/1000
minPW = (1.0 - correction)/1000

#servo = Servo(GPIO, min_pulse_width = minPW, max_pulse_width = maxPW)
servo=Servo

i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

sensor.sealevel_pressure = 102574
time.sleep(0.5)

alt = [] # array for altitude values
lv = sensor.altitude # initial value; zeroes it; 'launch value'

while True:
	altitude = sensor.altitude - lv
        # altitude is the diff between initial alt and current alt
	alt.append(altitude)
        # add latest data to alt array

	print(alt) # print array
	print(alt[0]) # print first altitude

	if altitude > 1: # if length of array is greater than 1
		pigs (s, 18, 2000) # spin fast clockwise
		time.sleep(200)
		pigs (s, 18, 1500)
