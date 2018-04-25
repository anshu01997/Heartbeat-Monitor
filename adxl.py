# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer
import time
import adxl345 
  
accel = adxl345.ADXL345()
while True: 
	axes = accel.getAxes(True)
	print "ADXL345 on address 0x%x:" % (adxl345.address)
	print "   x = %.3fG" % ( axes['x'] )
	print "   y = %.3fG" % ( axes['y'] )
	print "   z = %.3fG" % ( axes['z'] )
	time.sleep(5)
