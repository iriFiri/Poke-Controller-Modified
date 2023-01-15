#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from Commands.Keys import Button, Direction, Stick
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand




class AutoChantSpam(PythonCommand):
    NAME = 'AutoChantSpam'

    def __init__(self):
        super().__init__()

    def do(self):
        on = True

        print("Starting autochant")
        while on:
                self.press(Button.Y, wait=.4)
                sleep(5)



        #chant here forx
        print("Starting autochant")
        qty = 0
        while qty < 10:
                self.press(Button.Y, wait=.4)
                sleep(3)
                qty += 1

