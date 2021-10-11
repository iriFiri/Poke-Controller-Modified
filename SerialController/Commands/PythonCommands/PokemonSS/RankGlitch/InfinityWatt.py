#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand


# Get watt automatically using the glitch
class InfinityWatt(ImageProcPythonCommand):
    NAME = '無限ワット'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.use_rank = False
        self.path = 'PokemonSS/InfinityWatt'
        self.lang = 'JPN'

    def do(self):
        while True:
            self.wait(1)

            if self.use_rank:
                self.timeLeap()

                self.press(Button.A, wait=1)
                self.press(Button.A, wait=1)  # 2000W
                self.press(Button.A, wait=1.8)
                self.press(Button.B, wait=1.5)

            else:
                while not self.isContainTemplate(f'{self.path}/time_remaining_{self.lang}.png'):
                    self.press(Button.A, wait=0.9)

                self.timeLeap(is_go_back=False)
                
                self.press(Button.B, wait=1)
                self.press(Button.A, wait=6)  # レイドをやめる
