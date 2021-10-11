#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Hat, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


class AutoRaid_catch(ImageProcPythonCommand):
    NAME = 'AutoRaid_catch'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.cam_id = 2
        self.path = 'PokemonSS/AutoRaid_catch'
        self.lang = 'JPN'

        self.success = 0
        self.faild = 0

    def do(self):
        while True:
            self.entry()
            result = self.battle()
            if result:
                print(f'success: {self.success}, faild: {self.faild}')
                self.finish()
            else:
                self.reset_game()
                self.faild += 1

    def entry(self):
        while not self.isContainTemplate(f'{self.path}/challenge_{self.lang}.png'):
            self.press(Button.A, wait=1)
            
        self.press(Hat.BTM, wait=0.5)
        self.press(Button.A, wait=1)
        return

    def battle(self):
        while not self.isContainTemplate(f'{self.path}/win_{self.lang}.png'):
            self.press(Button.A, wait=0.5)
                
        while not self.isContainTemplate(f'{self.path}/catch_{self.lang}.png'):
            self.wait(1)

        self.press(Button.A, wait=0.5)
        self.press(Hat.LEFT, wait=0.5)
        self.press(Button.A, wait=0.5)

        while True:
            if self.isContainTemplate(f'{self.path}/faild_{self.lang}.png'):
                return False
            if self.isContainTemplate(f'{self.path}/success_{self.lang}.png'):
                return True
            self.wait(0.5)

    def reset_game(self):
        self.press(Button.HOME, wait=1.0)
        self.press(Button.X, wait=0.5)
        self.press(Button.A, wait=5.0)
        self.press(Button.A, wait=1.5)
        self.press(Button.A, wait=0.5)

        while not self.isContainTemplate(f'{self.path}/OP.png', threshold=0.6):
            self.wait(0.7)
            
        self.press(Button.A, wait=6.0)
        return
