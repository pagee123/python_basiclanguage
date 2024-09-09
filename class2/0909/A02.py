import RPi.GPIO as GPIO
import time

ledPin1=29
ledPin2=31
ledPin3=26
ledPin4=24
ledPin5=21
ledPin6=19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.setup(ledPin3,GPIO.OUT)
GPIO.setup(ledPin4,GPIO.OUT)
GPIO.setup(ledPin5,GPIO.OUT)
GPIO.setup(ledPin6,GPIO.OUT)

try:
    while(True):
        GPIO.output(ledPin1,False)
        GPIO.output(ledPin2,False)
        GPIO.output(ledPin3,False)
        GPIO.output(ledPin4,False)
        GPIO.output(ledPin5,False)
        GPIO.output(ledPin6,False)
        time.sleep(1)
        GPIO.output(ledPin1,True)
        GPIO.output(ledPin2,True)
        GPIO.output(ledPin3,True)
        GPIO.output(ledPin4,True)
        GPIO.output(ledPin5,True)
        GPIO.output(ledPin6,True)
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    