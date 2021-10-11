#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Direction, Hat
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


# Get watt automatically using the glitch
class autoraid_kocha(ImageProcPythonCommand):
    NAME = 'レイド周回[こちゃ]'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.cam_id = 2
        self.lang = 'JPN'

        self.success = 0
        self.faild = 0

    def do(self):
        while(True):
            print("------------------------")
            print(f'success: {self.success}, faild: {self.faild}')
            try:
                self.press(Button.Y, wait=1.5)
                self.press(Button.X, wait=1)
                self.press(Direction.LEFT, wait=1)
                while not self.isContainTemplate(f'PokemonSS/AutoRaid_kocha/kocha_raid_{self.lang}.png', threshold=0.95):
                    self.press(Button.X, wait=0.3)
                
                while not self.isContainTemplate('PokemonSS/AutoRaid_kocha/pass_input.png'):
                    self.press(Button.A, wait=0.4)

                self.press(Button.B)    
                self.press(Hat.BTM, wait=0.1)
                self.press(Hat.BTM, wait=0.1)
                self.press(Button.A)
                self.press(Hat.TOP, wait=0.1)
                self.press(Button.A)
                self.press(Hat.TOP, wait=0.1)
                self.press(Button.A)
                self.press(Button.A)

                self.press(Hat.BTM, wait=0.1)
                self.press(Hat.BTM, wait=0.1)
                self.press(Button.A)
                self.press(Hat.TOP, wait=0.1)
                self.press(Button.A)
                self.press(Hat.TOP, wait=0.1)
                self.press(Button.A)
                self.press(Button.A)

                self.press(Button.PLUS, wait=5)

                self.press(Button.A, wait=2)
                
                if self.isContainTemplate(f'PokemonSS/AutoRaid_kocha/faild_{self.lang}.png'):
                    print('faild...')
                    self.press(Button.A, wait=5)
                    self.faild += 1
                    continue

                print('fight !')
                while not self.isContainTemplate(f'PokemonSS/AutoRaid_kocha/win_{self.lang}.png'):
                    self.press(Button.A, wait=1)

                print('win !!')
                self.success += 1
                
                while not self.isContainTemplate(f'PokemonSS/AutoRaid_kocha/catch_{self.lang}.png'):
                    self.wait(1)
                    
                self.press(Hat.BTM)
                self.press(Button.A, wait=0.5)
                    
                while not self.isContainTemplate('PokemonSS/AutoRaid_kocha/online.png'):
                    self.press(Button.A, wait=0.5)
            except cv2.error as e:
                self.LINE_text(f'cv2.error\nsuccess: {self.success}\nfaild: {self.faild}')
                raise StopThread
