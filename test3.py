import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(37, GPIO.IN)

while GPIO.input(37) == 0:

while GPIO.input(37) == 1:
    print("Received")
    
    GPIO.cleanup()
