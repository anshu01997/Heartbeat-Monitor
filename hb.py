
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(40,GPIO.IN)
count1 =0
# read data after 10 seconds
time.sleep(10)
while (1):
        time.sleep(0.1)
        a= GPIO.input(40)
        if (a==1):
                count1=count1+1
                print (count1)
