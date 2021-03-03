import RPi.GPIO as GPIO
from time import sleep
from AMSpi import AMSpi as amspi
from gpiozero import DistanceSensor

TRIG = 4
ECHO = 17
sensor = DistanceSensor(ECHO, TRIG)


# For BOARD pin numbering use AMSpi(True) otherwise BCM is used

# Set PINs for controlling shift register (GPIO numbering)
amspi.set_74HC595_pins(21, 20, 16)
# Set PINs for controlling all 4 motors (GPIO numbering)
amspi.set_L293D_pins(5,6)
# Run motors
amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
	
def turnL(x):
	amspi.run_dc_motors([amspi.DC_Motor_1], clockwise=False)
	amspi.run_dc_motors([amspi.DC_Motor_2])
	sleep(x)
	amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])	
def turnR(x):
	amspi.run_dc_motors([amspi.DC_Motor_2], clockwise=False)
	amspi.run_dc_motors([amspi.DC_Motor_1])
	sleep(x)
	amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
def goTo(x):
	amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
	sleep(x)
def stopM():
	amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
def backTo(x):
	amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2], clockwise=False)
	sleep(x)
	amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
	
def volverCamino(c):
	goto(4)
	if c<0:
		turnR(6)
		goTo(4)
		turnL(3)
	if c>0:
		turnL(6)
		goTo(4)
		turnR(3)

try:
	while True:
		c=0
		goTo(2)
		if sensor.distance < 0.15:
			stopM()
			turnL(3)
			c=-1
		if sensor.distance < 0.15:
			turnR(6)
			c=1
		if sensor.distance < 0.15:
			turnL(3)
			c=0
			backTo(4)
			turnL(3)
			c=-1
		volverCamino(c)


	
	
	
	
