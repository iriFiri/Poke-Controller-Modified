#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Hat, Direction, Stick, Tilt

class D2RBase(PythonCommand):
	NAME = 'D2RBase'

	def __init__(self):
		super().__init__()

	def stick(self, buttons, duration=0.1, wait=0.1):
		self.keys.input(buttons, ifPrint=False)
		self.wait(duration)
		self.wait(wait)
		self.checkIfAlive()	

	def do(self):
		self.startGame()
		self.wait(40) #30 seconds? need load screen check
		self.claimBody()
		self.moveTesty(245, 1, 6.1)
		#use red portal
		self.attackTk()
		#load
		sleep(3)
		#self.wait(2) #need load screen check
		#face toward pindle
		self.moveTesty(65, .1, .1)
		#3x tele
		self.attackTele()
		self.wait(.2)
		self.attackTele()
		self.wait(.2)
		self.attackTele()
		#attack pindle here
		
		self.useMP()
		self.moveTesty(15, .1, .1)
		j=0
		while j < 10:
		
			self.moveTesty(15, .1, .1)
			self.attackBlizz()
			self.attackGlac()
			self.attackGlac()
			j+=1

		self.quitGame()
		#pass


	'''
	first move
	245 for 5s?
	take red port
	tele 2 or 3 times?
	begin attack spam
	moveTo items
	choose pick
	exit

	'''
	#starting a game from the char select screen
	def startGame(self):
		print("Starting Game")
		self.press(Hat.TOP)
		self.press(Hat.TOP)
		self.press(Hat.TOP)
		self.press(Hat.TOP)
		self.press(Button.A)
		self.press(Button.A)
		#place diff var here
		self.press(Hat.BTM)
		self.press(Hat.BTM)
		self.press(Button.A)
		#now loads

	#quiting the current game
	def quitGame(self):
		print("Quiting Game")
		self.press(Button.PLUS)
		self.press(Button.R)
		self.press(Button.R)
		self.press(Hat.BTM, wait=0.1)
		self.press(Button.A)
		self.wait(3)
		self.press(Hat.TOP)

	#grab body when standing on it
	def claimBody(self):
		print("Claiming Body")
		self.press(Button.A)

	#Use Telekinese
	def attackTk(self):
		print("Using TK")
		self.press(Button.R)

	#Use Teleport
	def attackTele(self):
		print("Using Teleport")
		self.press(Button.ZR)

	#Use Blizz
	def attackBlizz(self):
		print("Using Blizz")
		self.press(Button.B)

	#Use Glac
	def attackGlac(self):
		print("Using Glac")
		self.press(Button.A)

	#Use MP
	def useMP(self):
		print("Using MP")
		self.press(Hat.TOP)

	#Use HP
	def useHP(self):
		print("Using HP")
		self.press(Hat.LEFT)

	

	#testing movement
	def moveTesty(self, degree, speed, hold):
		print(f"moveing {degree} for {hold}s at {speed}")
		duration = hold
		angle = degree #angle
		r = speed #speed
		self.stick(Direction(Stick.LEFT, angle, r, showName=f'Angle={angle},r={r}'), duration, wait=0.0)

		#self.press(Button.A)