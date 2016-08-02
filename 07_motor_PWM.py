#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

MotorPin1   = 11    # pin11
MotorPin2   = 12    # pin12
MotorPWM = 13    # pin13


def setup():
	GPIO.setmode(GPIO.BOARD)          # Numbers GPIOs by physical location
	GPIO.setup(MotorPin1, GPIO.OUT)   # mode --- output
	GPIO.setup(MotorPin2, GPIO.OUT)
	GPIO.setup(MotorPWM, GPIO.OUT)

def loop():
	p = GPIO.PWM(MotorPWM, 1000)     # set Frequece to 1KHz
	p.start(0)
	while True:
		print 'Press Ctrl+C to end the program...'
		p.ChangeDutyCycle(50)
		GPIO.output(MotorPin1, GPIO.HIGH)  # clockwise
		GPIO.output(MotorPin2, GPIO.LOW)
		time.sleep(5)
		
		p.ChangeDutyCycle(0) # motor stop
		time.sleep(5)
		
		p.ChangeDutyCycle(100)		
		GPIO.output(MotorPin1, GPIO.LOW)   # anticlockwise
		GPIO.output(MotorPin2, GPIO.HIGH)
		time.sleep(5)
		
		p.ChangeDutyCycle(0) # motor stop
		time.sleep(5)

def destroy():
	GPIO.output(MotorPWM, GPIO.LOW) # motor stop
	GPIO.setup(MotorPWM, GPIO.IN)
        GPIO.setup(MotorPin1, GPIO.IN)   # mode --- output
        GPIO.setup(MotorPin2, GPIO.IN)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

