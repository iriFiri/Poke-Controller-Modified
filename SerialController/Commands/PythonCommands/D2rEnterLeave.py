#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Hat, Direction, Stick, Tilt

class D2RFind(ImageProcPythonCommand):
	NAME = 'd2rEnterLeave'

	def __init__(self, cam):
		super().__init__(cam)


	def stick(self, buttons, duration=0.1, wait=0.1):
		self.keys.input(buttons, ifPrint=False)
		self.wait(duration)
		self.wait(wait)
		self.checkIfAlive()	

	def do(self):
		#self.startGame()
		self.quitGame()

	def quitGame(self):
		print("Quiting Game")
		if self.isContainTemplate('deathCheck.png'):
			print("Death Check")
			self.press(Button.PLUS)
			self.wait(.2)
			while not (self.isContainTemplate('loadCheck2.png') or self.isContainTemplate('loadCheck.png')):
				print("Still Loading")
			self.wait(1)

		self.press(Button.PLUS)
		print("pressing plus")
		while not self.isContainTemplate('optionsMenu.png'):
			if not self.isContainTemplate('menuCheck.png', threshold=0.9):
				self.press(Button.PLUS)
				print("pressing plus")
			print("changing to options")
			self.press(Button.R)
			self.wait(.2)
		
		while self.isContainTemplate('menuCheck.png'):
			if not self.isContainTemplate('exitOption.png', threshold=0.9):
				print("down on options")
				self.press(Hat.BTM, wait=0.1)
				self.wait(.2)
			else:
				print("exit")
				self.press(Button.A)
		self.wait(3)
		self.press(Hat.TOP)

		#starting a game from the char select screen
	def startGame(self):
		print("Starting Game")
		self.press(Button.A)
		#self.wait(1)
		self.press(Button.A)
		#place diff var here
		self.wait(2)
		self.press(Button.B)
		self.press(Button.A)
		print("Pressing down now")

		self.press(Hat.BTM)
		self.press(Hat.BTM)
		while not self.isContainTemplate('helldif.png'):
			print("pressing down agian")
			self.press(Hat.BTM)
		self.press(Button.A)		
		#now loads

	#testing movement
	def moveTesty(self, degree, speed, hold):
		print(f"moveing {degree} for {hold}s at {speed}")
		duration = hold
		angle = degree #angle
		r = speed #speed
		self.stick(Direction(Stick.LEFT, angle, r, showName=f'Angle={angle},r={r}'), duration, wait=0.0)

		#self.press(Button.A)