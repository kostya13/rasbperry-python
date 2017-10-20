import RPi.GPIO as GPIO   
from time import sleep
GPIO.setmode(GPIO.BOARD)    #устанавливаем режим нумерации
Data = 3
Latch = 5
Clock = 7
GPIO.setup(Data, GPIO.IN, pull_up_down=GPIO.PUD_OFF)    #Data
GPIO.setup(Latch, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)   #Latch
GPIO.setup(Clock, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)   #Clock
GPIO.output(Latch, False) 
GPIO.output(Clock, False)
try:
	while True:
		GPIO.output(Latch, True) 
		sleep(0.01)
		GPIO.output(Latch, False) 
		buttons = []
		for i in range(8):
			signal = GPIO.input(Data)
			buttons.append(signal)
			GPIO.output(Clock, True) 
			GPIO.output(Clock, False) 
		print(buttons)
finally:
	GPIO.cleanup()                        #завершаем работу с GPIO

