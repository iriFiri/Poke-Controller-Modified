#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Hat, Direction, Stick, Tilt
import numpy
import math

class D2RFind(ImageProcPythonCommand):
	NAME = 'd2rMove'

	def __init__(self, cam):
		super().__init__(cam)


	def stick(self, buttons, duration=0.1, wait=0.1):
		self.keys.input(buttons, ifPrint=False)
		self.wait(duration)
		self.wait(wait)
		self.checkIfAlive()	

	def do(self):	
		
		self.bluePortal()
		print("done")
		self.moveCenter()

		'''	
		self.press(Button.LCLICK, 4, .1)
		class Cord:
			def __init__(self, x, y):
				self.x = x
				self.y = y
				'''

	def bluePortal(self):
		print("Waiting for TP")
		
		while not self.isContainTemplate('TakeBlueTP.png', threshold=0.9):
			print("Waiting for TP")
			self.wait(.5)
			
		print("taking TP")
		self.press(Button.A)
		self.wait(1)
		while not (self.isContainTemplate('loadCheck2.png') or self.isContainTemplate('loadCheck.png')):
			#print("Still Loading")
			self.wait(1)
		print("Done taking")

	def moveCenter(self):
		
		self.moveTesty(180, 1, 2.7)
		self.moveTesty(135, 0, .1) #STOP INPUT
		'''		
		center = Cord(640, 360)


		dX = 91
		while dX > 90:
			res = self.isContainTemplate('rune.png', threshold=0.6)
			fImage = Cord(res[0],res[1])
			dist = Cord(fImage.x - center.x, fImage.y - center.y)
			#print("pre dist calc")
			tDist = self.calcDist(center, fImage)
			dX = tDist
			bearing = numpy.arctan2(dist.x, dist.y)
			bearing = numpy.degrees(bearing)
			bearing = bearing + 270
			#print(f"heading = {str(bearing)}")
			self.moveTesty(bearing, .75, .1)




		class Cord:
			def __init__(self, x, y):
				self.x = x
				self.y = y
				
		center = Cord(640, 360)
		dX = 91
		print("Attempting Loot")	
		self.press(Button.X)
		self.wait(1)	
		while self.isContainTemplate('Rune.png', threshold=0.6):
			print("Trying to Loot")
			while dX > 90:
				res = self.isContainTemplate('Rune.png', threshold=0.6)
				fImage = Cord(res[0],res[1])
				dist = Cord(fImage.x - center.x, fImage.y - center.y)
				#print("pre dist calc")
				tDist = self.calcDist(center, fImage)
				dX = tDist
				bearing = numpy.arctan2(dist.x, dist.y)
				bearing = numpy.degrees(bearing)
				bearing = bearing + 270
				#print(f"heading = {str(bearing)}")
				self.moveTesty(bearing, .25, .1)
			
				self.press(Button.A)
		self.press(Button.X)	
		self.wait(1)	
		while self.isContainTemplate('Rune.png', threshold=0.6):
			print("Trying to Loot")
			while dX > 90:
				res = self.isContainTemplate('Rune.png', threshold=0.6)
				fImage = Cord(res[0],res[1])
				dist = Cord(fImage.x - center.x, fImage.y - center.y)
				#print("pre dist calc")
				tDist = self.calcDist(center, fImage)
				dX = tDist
				bearing = numpy.arctan2(dist.x, dist.y)
				bearing = numpy.degrees(bearing)
				bearing = bearing + 270
				#print(f"heading = {str(bearing)}")
				self.moveTesty(bearing, .25, .1)
				self.press(Button.A)

'''


	def calcDist(self, pointA, pointB):
		return (
		((pointA.x - pointB.x) ** 2) +
		((pointA.y - pointB.y) ** 2)
		) ** 0.5
		

	#testing movement
	def moveTesty(self, degree, speed, hold):
		print(f"moveing {degree} for {hold}s at {speed}")
		duration = hold
		angle = degree #angle
		r = speed #speed
		self.stick(Direction(Stick.LEFT, angle, r, showName=f'Angle={angle},r={r}'), duration, wait=0.0)
		return
		#self.press(Button.A)


		