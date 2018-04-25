import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(04,GPIO.IN)
count1=0
time.sleep(10)
time_end=time.time()+60
while(time.time()<time_end):
    time.sleep(0.1)
    
    if(GPIO.input(04)== True):
        count1=count1+1
        print(count1)

    else:
        print('no input')

print('bpm:')
print(count1)
