# -*- coding: utf-8 -*-
#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import smbus
import time

# ADXL345 Class
class ADXL345():
	DevAdr = 0x1D
	myBus = ""
	if GPIO.RPI_INFO['P1_REVISION'] == 1:
		myBus = 0
	else:
		myBus = 1
	b = smbus.SMBus(myBus)

	def setUp(self):
		self.b.write_byte_data(self.DevAdr, 0x2C, 0x0B) # BandwidthRate
		self.b.write_byte_data(self.DevAdr, 0x31, 0x00) # DATA_FORMAT 10bit 2g
		self.b.write_byte_data(self.DevAdr, 0x38, 0x00) # FIFO_CTL OFF
		self.b.write_byte_data(self.DevAdr, 0x2D, 0x08) # POWER_CTL Enable

	def getValueX(self):
		return self.getValue(0x32)

	def getValueY(self):
		return self.getValue(0x34)

	def getValueZ(self):
		return self.getValue(0x36)

	def getValue(self, adr):
		tmp = self.b.read_byte_data(self.DevAdr, adr+1)
		sign = tmp & 0x80
		tmp = tmp & 0x7F
		tmp = tmp<<8
		tmp = tmp | self.b.read_byte_data(self.DevAdr, adr)
#		print '%4x' % tmp # debug

		if sign > 0:
			tmp = tmp - 32768

		return tmp

#	tmp = self.b.read_word_data(self.DevAdr, adr)

# MAIN
myADXL345 = ADXL345()
myADXL345.setUp()

# LOOP
for a in range(1000):
	x = myADXL345.getValueX()
	y = myADXL345.getValueY()
	z = myADXL345.getValueZ()
	os.system("clear")
	print("X=", x)
	print("Y=", y)
	print("Z=", z)
	time.sleep(0.5)
