import RPi.GPIO as gpio
from time import sleep
from gpiozero import DistanceSensor

TRIG = 4
ECHO = 17
sensor = DistanceSensor(ECHO, TRIG)

inA1 = 5
inA2 = 6
inB1 = 13
inB2 = 26

gpio.setup(inA1, gpio.out)
gpio.setup(inA2, gpio.out)
gpio.setup(inB1, gpio.out)
gpio.setup(inB2, gpio.out)

sleep(2)
	
def turnL(x):
	gpio.output(inA1, gpio.LOW)
	gpio.output(inB1, gpio.HIGH)
	gpio.output(inA2, gpio.HIGH)
	gpio.output(inB2, gpio.LOW)
	sleep(x)
	gpio.output(inB1, gpio.LOW)
	gpio.output(inA2, gpio.LOW)
def turnR(x):
	gpio.output(inA1, gpio.HIGH)
	gpio.output(inB1, gpio.LOW)
	gpio.output(inA2, gpio.LOW)
	gpio.output(inB2, gpio.HIGH)
	sleep(x)
	gpio.output(inA1, gpio.LOW)
	gpio.output(inB2, gpio.LOW)
def goTo(x):
	gpio.output(inA1, gpio.HIGH)
	gpio.output(inB1, gpio.HIGH)
	gpio.output(inA2, gpio.LOW)
	gpio.output(inB2, gpio.LOW)
	sleep(x)
def stopM():
	gpio.output(inA1, gpio.LOW)
	gpio.output(inB1, gpio.LOW)
	gpio.output(inA2, gpio.LOW)
	gpio.output(inB2, gpio.LOW)
def backTo(x):
	gpio.output(inA1, gpio.LOW)
	gpio.output(inB1, gpio.HIGH)
	gpio.output(inA2, gpio.LOW)
	gpio.output(inB2, gpio.HIGH)
	sleep(x)
	gpio.output(inB1, gpio.LOW)
	gpio.output(inB2, gpio.LOW)
	
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


	
	
	
	
