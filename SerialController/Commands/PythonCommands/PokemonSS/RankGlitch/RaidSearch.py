#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand


# Get watt automatically using the glitch
class RandSearch(ImageProcPythonCommand):
    NAME = ''

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.use_rank = False
        self.leap_times = 3


    def do(self):
        count = 0
        while count < leap_times:
            self.wait(1)
            
            if self.use_rank:
                self.timeLeap()

                self.press(Button.A, wait=1)
                self.press(Button.A, wait=1)  # 2000W
                self.press(Button.A, wait=1.8)
                self.press(Button.B, wait=1.5)

            else:
                while not self.isContainTemplate('Raid_en.png'):
                    self.press(Button.A, wait=1)

                self.timeLeap(is_go_back=False)
                
                self.press(Button.B, wait=1)
                self.press(Button.A, wait=6)  # レイドをやめる

            count += 1
