import serial 
import time 
import RPi.GPIO as GPIO 
port = serial.Serial("/dev/ttyS0", 9600, timeout=3.0) 
print"GSM 300\n" 
print"List of operating Commands" 
print"Commands		functions" 
print"AT	to check operations" 
port.write('AT\r')		
rcv = port.read(20) 
print"GSM" + rcv
try:
            print "Sending Message...."
            msg1 = "Emergency http://www.google.com/maps/place/49.46800006494457,17.11514008755796"
            port.write('AT+CMGF=1'+'\r')
            number = raw_input("Enter Mobile: ")
            port.write('AT+CMGS="'+number+'"\r')
            time.sleep(2)
            port.write(msg1)
            time.sleep(2)
            port.write('\x1A\r')
            print port.read(50)
except:
            port.close()
            

        
