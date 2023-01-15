#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Hat, Direction, Stick, Tilt

class D2Rimg(ImageProcPythonCommand):
	NAME = 'D2Rimg'

	def __init__(self, cam):
		super().__init__(cam)



	def do(self):
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

