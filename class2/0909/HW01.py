import RPi.GPIO as GPIO
import time

ledsPin=5
ledePin=10
lightPin=ledsPin
GPIO.setmode(GPIO.BCM)
for i in range(5,11):
    GPIO.setup(i,GPIO.OUT)
try:
    while(True):
        for i in range(5,11):
            GPIO.output(i,True)
        GPIO.output((lightPin%6)+5,False)
        GPIO.output(((lightPin+1)%6)+5,False)
        GPIO.output(((lightPin+2)%6)+5,False)
        if(lightPin<ledePin):
            lightPin+=1
        else:
            lightPin=ledsPin
        time.sleep(0.7)
        
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
    