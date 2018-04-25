import serial 
import time 
import RPi.GPIO as GPIO 
port = serial.Serial("/dev/ttyS0", 9600, timeout=3.0) 
try: 
	print"GSM 300\n" 
	print"List of operating Commands" 
	print"Commands		functions" 
	print"AT	to check operations" 
	port.write('AT\r\n')		
	rcv = port.read(20) 
	print"GSM" + rcv
	while True: 
		        rcv = port.read(20) 
		        print rcv
		        time.sleep(2) 
		
			keyin=raw_input("want to call? press y else n")
			if(keyin=='y'):
                                keyin=raw_input("dial number:")
			        print keyin
			        keyin2 = 'ATD '+keyin+';\r\n' 
			        print"Dialing : " + keyin2
			        port.write(keyin2)
			        time.sleep(2)
		                #x=1 
		                #for x in range(0,9): 
			          # rcv= port.read(50) 
			          # print rcv
			        #x+=1
                                keyin = raw_input("Type ATH or ath to cut call")
			        port.write(keyin+'\r\n')

                        else:
                                        if keyin == "n" or "N":
                                                rcv = port.read(20) 
                                                print rcv
                                                time.sleep(2)

		        if rcv=='RING':			
			    print 'ring' 
			    port.write('ATH \r\n') 
except: 
	port.close() 


