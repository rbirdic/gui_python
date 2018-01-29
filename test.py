import RPi.GPIO as GPIO
import time
 
pinList = [3,5,7,8,10,11,12,
           13,15,16,18,19,21,
           22,23,24,26,29,31,
           32,33,35,36,37,38,40]

f = open("results.txt", "w+")
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(32, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(36, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(38, GPIO.IN)

while 1:
    for x in range(0, 16):
        if GPIO.input(pinList[x])==1 :
            print ("It was pin %d\n" % (pinList[x]))
            f.write ("It was pin %d\n" % (pinList[x]))
GPIO.cleanup()
