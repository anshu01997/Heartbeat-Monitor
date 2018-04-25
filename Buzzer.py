from gpiozero import Buzzer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
buzzer = Buzzer(20)
count1 =0
# read data after 10 seconds
time.sleep(10)
buzzer.on()
time.sleep(1)
buzzer.off()

