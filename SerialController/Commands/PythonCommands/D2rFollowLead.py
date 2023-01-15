#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Hat, Direction, Stick, Tilt, SendFormat
import numpy
class D2RFind(ImageProcPythonCommand):
	NAME = 'd2rFollowLead'

	def __init__(self, cam):
		super().__init__(cam)


	def stick(self, buttons, duration=0.1, wait=0.1):
		self.keys.input(buttons, ifPrint=False)
		self.wait(duration)
		self.wait(wait)
		self.checkIfAlive()	

	def do(self):
		botGo = True
		
		print("Launch")
		while botGo:
			self.runBot()
			botGo = True

	def runBot(self):
		
		#print("Begining")
			# while not self.isContainTemplate('charSelect.png', threshold=0.4):
			# 	#print("Waiting for Character Screen")
			# 	if self.isContainTemplate('deathCheck.png'):
			# 		self.quitGame()
			# 	self.wait(1)
			# self.wait(1)
			# self.startGame()
		while not (self.isContainTemplate('gotInvite.png') or self.isContainTemplate('gotInvite.png')):
			print("wait")
			self.wait(1)
			print("wait done")

		print("join")	
		self.joinGame()

		while not (self.isContainTemplate('loadCheck2.png') or self.isContainTemplate('loadCheck.png')):
			#print("Still Loading")
			self.wait(1)
		self.claimBody()
		self.beltFill()
		
		#invite friends
		#self.invite()

		#use wait for blue port
		self.bluePortal()


		self.wait(2)
		#self.moveTesty(225, 2, 1)
		#self.moveTesty(90, .1, .1)
		#self.moveTesty(90, 0, .1)
		#self.moveTesty(90, .1, .1)

		## enter bottom left
		self.moveTesty(150, 1, 1.5)
		self.moveTesty(60, 1, 2.5)
		self.moveTesty(60, 0, .1)

		while self.isContainTemplate('leader.png', threshold=0.6):
			
			self.attackBlizz()
			self.wait(.25)
			self.attackGlac()
			self.wait(.25)


		self.quitGame()
		#pass
			
		#pass

	def invite(self):
		print("Inviting")
		self.press(Button.PLUS)
		self.wait(.5)
		self.press(Button.L)
		self.press(Button.L)
		self.press(Button.L)
		self.wait(.5)
		#open FL
		self.press(Button.MINUS)
		self.press(Button.Y)
		self.wait(1)
		
		print("Looking for confirm")
		while not self.isContainTemplate('sent.png'):
			self.wait(.5)
		#close confirm	
		print("close confirm")
		self.wait(.5)
		self.press(Button.B)
		self.wait(1)
		self.press(Button.B)

	def bluePortal(self):
		print("Waiting for TP")
		
		while not self.isContainTemplate('TakeBlueTP.png', threshold=0.9):
			#print("Waiting for TP")
			self.wait(.5)
			
		print("taking TP")
		self.wait(2)
		self.press(Button.A)
		self.wait(1)
		while not (self.isContainTemplate('loadCheck2.png') or self.isContainTemplate('loadCheck.png')):
			#print("Still Loading")
			self.wait(1)
		print("Done taking")
	
	def moveCenter(self):
		
		self.moveTesty(180, 1, 2.7)
		self.moveTesty(135, 0, .1) #STOP INPUT

	#starting a game from the char select screen
	def startGame(self):
		#print("Starting Game")
		self.press(Button.A)
		self.wait(.5)
		self.press(Button.A)
		self.wait(.5)

		self.selectDiff()
		self.wait(1)
		
		#print("back in startGame")

		#self.press(Button.A)
		#now loads
	def joinGame(self):
		print("Joining Game")
		self.press(Button.HOME)
		self.wait(2)
		self.press(Button.A)
		self.wait(2)
		while not self.isContainTemplate('charSel.png'):
			self.wait(.5)
		self.press(Button.A)
		self.wait(2)
		self.press(Button.A)
		self.wait(2)


	def selectDiff(self):
		#print("selecting diff")
		while self.isContainTemplate('selectDiff.png'):
			if not self.isContainTemplate('ftj.png'):
				if self.isContainTemplate('helldif.png', threshold=0.9):
					#print("Found hell - selecting")
					self.press(Button.A)
					self.wait(2)						
				elif self.isContainTemplate('normdif.png', threshold=0.9):
					#print("Norm diff found - pressing down agian")
					self.moveTesty(270, 1, 1)
					#self.moveTesty(270, 1, 2)
					self.moveTesty(270, 0, .2)
				elif self.isContainTemplate('nightdif.png', threshold=0.9):
					#print("Night diff found - pressing down agian")
					self.moveTesty(270, 1, 1)
					#self.moveTesty(270, 1, 2)
					self.moveTesty(270, 0, .2)
			else:
				#print("ftj - retry")
				self.press(Button.A)
				self.wait(2)
			self.wait(2)

	def beltFill(self):
		self.press(Button.PLUS)
		self.press(Button.RCLICK, 2, .1)
		self.press(Button.B)
		self.press(Button.B)
		self.press(Button.B)

	#quiting the current game
	def quitGame(self):
		#print("Quiting Game")
		if self.isContainTemplate('deathCheck.png'):
			#print("Death Check")
			self.press(Button.PLUS)
			self.wait(.2)
			while not (self.isContainTemplate('loadCheck2.png') or self.isContainTemplate('loadCheck.png')):
				#print("Still Loading")
				if self.isContainTemplate('gamma.png'):
					self.press(Button.B)
					self.wait(.1)
					self.press(Button.B)
					self.wait(.1)
					self.press(Button.B)

			self.wait(1)

		self.press(Button.PLUS)
		#print("pressing plus")
		while not self.isContainTemplate('optionsMenu.png'):
			if not self.isContainTemplate('menuCheck.png', threshold=0.9):
				self.press(Button.PLUS)
				#print("pressing plus")
			#print("changing to options")
			self.press(Button.R)
			self.wait(.25)
		
		while self.isContainTemplate('menuCheck.png'):
			if not self.isContainTemplate('exitOption.png', threshold=0.9):
				#print("down on options")
				self.press(Hat.BTM, wait=0.1)
				self.wait(.25)
			else:
				#print("exit")
				self.press(Button.A)
		self.wait(3)
		self.press(Hat.TOP)

	#grab body when standing on it
	def claimBody(self):
		#print("Claiming Body")
		self.press(Button.A)

	#Use Telekinese
	def attackTk(self):
		#print("Using TK")
		self.press(Button.R)

	#Use Teleport
	def attackTele(self):
		#print("Using Teleport")
		self.press(Button.ZR)

	#Use Blizz
	def attackBlizz(self):
		#print("Using Blizz")
		self.press(Button.B)
			
	#Use Redemption
	def attackRedem(self):
		#print("Using Redemption")
		self.press(Button.ZR)
			
	#Use Hammbers
	def attackHammer(self):
		#print("Using Blizz")
		self.press(Button.B, 6, 1)

	#Use Glac
	def attackGlac(self):
		#print("Using Glac")
		self.press(Button.Y)

	#Use MP
	def useMP(self):
		#print("Using MP")
		self.press(Hat.TOP)

	#Use HP
	def useHP(self):
		#print("Using HP")
		self.press(Hat.LEFT)

	#Loot
	def loot(self):

		class Cord:
			def __init__(self, x, y):
				self.x = x
				self.y = y
				
		center = Cord(640, 360)
		dX = 91
		print("Attempting Loot")	
		self.press(Button.X)
		self.wait(1)
		self.moveTesty(20, 1, 1.1)
		self.moveTesty(20, 0, .1)	
		while self.isContainTemplate('rune.png'):
			#print("Trying to Loot")
			self.press(Button.A)
		self.press(Button.X)	
		self.wait(1)	
		while self.isContainTemplate('rune.png'):
			#print("Trying to Loot")
			#self.moveTesty(15, .25, 1)
			#self.moveTesty(15, 0, .1)
			self.press(Button.A)



	def calcDist(self, pointA, pointB):
		#print("dist calc")
		return (
		((pointA.x - pointB.x) ** 2) +
		((pointA.y - pointB.y) ** 2)
		) ** 0.5

	#testing movement
	def moveTesty(self, degree, speed, hold):
		#print(f"moveing {degree} for {hold}s at {speed}")
		duration = hold
		angle = degree #angle
		r = speed #speed
		self.stick(Direction(Stick.LEFT, angle, r, showName=f'Angle={angle},r={r}'), duration, wait=0.0)

	
	#testing movement
	def moveRS(self, degree, speed, hold):
		#print(f"moveing {degree} for {hold}s at {speed}")
		duration = hold
		angle = degree #angle
		r = speed #speed
		self.stick(Direction(Stick.RIGHT, angle, r, showName=f'Angle={angle},r={r}'), duration, wait=0.0)

		#self.press(Button.A)