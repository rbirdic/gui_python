import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(3, GPIO.IN)
GPIO.output(40, False)

print (GPIO.input(3))
GPIO.output(40, True)
print (GPIO.input(3))

GPIO.cleanup()
