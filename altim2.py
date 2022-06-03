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


#servo = Servo(GPIO, min_pulse_width = minPW, max_pulse_width = maxPW)
my_servo=Servo(18)

i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

sensor.sealevel_pressure = 102574
time.sleep(0.5)

my_servo.min()
alt = [] # array for altitude values
lv = sensor.altitude # initial value; zeroes it; 'launch value'

while True:
	altitude = sensor.altitude - lv
        # altitude is the diff between initial alt and current alt
	alt.append(altitude)
        # add latest data to alt array

	print(alt) # print array
	print(alt[0]) # print first altitude

	if altitude > 5: # if length of array is greater than 1
		print("servo fire")
		my_servo.max()
		time.sleep(5)
	else:
		my_servo.min()
		time.sleep(5)
