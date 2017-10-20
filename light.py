import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

SENSOR = 11 
GPIO.setup(SENSOR,GPIO.IN)
try:
	while True:
		print("Sensor status ", GPIO.input(SENSOR))
finally:
	GPIO.cleanup() 

