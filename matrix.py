import RPi.GPIO as GPIO   
from time import sleep
GPIO.setmode(GPIO.BOARD)   

def clean():
	for line in lines:
		dataline = line[2]
		clockline = line[1]
		resetline = line[0]
		GPIO.output(dataline, False)
		GPIO.output(clockline, False)
		GPIO.output(resetline, True)
		GPIO.output(resetline, False)

def setline(value):
	for i in reversed(value[:4]):
		data = i == '1'
		GPIO.output(D1, data)
		GPIO.output(C1, True)
		GPIO.output(C1, False)
	for i in reversed(value[4:]):
		data = i == '1'
		GPIO.output(D2, data)
		GPIO.output(C2, True)
		GPIO.output(C2, False)

def hide():
	for c in columns:
		GPIO.output(c, False) 

def show(col):
	c = '{0:04b}'.format(col)
	GPIO.output(Col8, c[0] == '1') 
	GPIO.output(Col4, c[1] == '1') 
	GPIO.output(Col2, c[2] == '1') 
	GPIO.output(Col1, c[3] == '1') 

def reset():
	GPIO.output(R1, True)
	GPIO.output(R1, False)
	GPIO.output(R2, True)
	GPIO.output(R2, False)


Col1 = 22
Col2 = 23
Col4 = 24
Col8 = 26
R1 = 13
C1 = 15
D1 = 16
R2 = 18
C2 = 19
D2 = 21
lines = ((R1, C1, D1), (R2, C2, D2))
columns = (Col1, Col2, Col4, Col8)
GPIO.setup(Col1, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(Col2, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(Col4, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(Col8, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(R1, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(C1, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(D1, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(R2, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(C2, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(D2, GPIO.OUT, pull_up_down=GPIO.PUD_OFF)

image = [ '00000000',
	  '00000000',
	  '00100000',
	  '00011000',
	  '11111100',
	  '00011000',
	  '00100000',
	  '00000000']
try:
	clean()
	while True:
		for i in range(0,8):
			hide()
			setline(image[i])
			show(i+1)
			sleep(0.002)
			reset()
finally:
	GPIO.cleanup()                        #завершаем работу с GPIO

