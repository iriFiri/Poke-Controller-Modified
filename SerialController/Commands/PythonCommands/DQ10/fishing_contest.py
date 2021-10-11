#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Hat, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


# Get watt automatically using the glitch
class fishing_contest(ImageProcPythonCommand):
    NAME = 'DQ10 釣りコンテスト'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.cam_id = 2

    def do(self):
#        self.move_natsuri()
        while True:
            self.fishing()
        # try:

        # except cv2.error as e:
        #     self.LINE_text(f"\n{e}\nprogram exit -1")
        #     raise StopThread
        
    def fishing(self):

        if self.isContainTemplate('DQ10/start.png'):
            print('start')
            self.press(Button.A, wait=1)
        else:
            print('faild')
            return

        while not self.isContainTemplate('DQ10/hit.png'):
            print('waiting...')
            self.wait(1)

        while not self.isContainTemplate('DQ10/command.png'):
            print('wait command')
            self.press(Button.A, wait=1)

        if self.isContainTemplate('DQ10/big_fish.png'):
            print('big fish !!')
            big_fish = True
        else:
            big_fish = False

        print('special attack')
        self.press(Hat.BTM, wait=1)
        self.press(Hat.BTM, wait=1)
        self.press(Hat.BTM, wait=1)

        self.battle()
        
        print('nomal attack')
        self.press(Hat.TOP, wait=1)
        self.press(Hat.TOP, wait=1)
        self.press(Hat.TOP, wait=1)

        while not self.battle():
            self.wait(0.5)
        
        while not self.isContainTemplate('DQ10/start.png'):
            self.press(Button.A, wait=1)
        
        return

    def battle(self):
        self.press(Button.A, wait=1)
        warning = False
        while not self.isContainTemplate('DQ10/command.png'):
            self.press(Button.A, wait=1.5)
            if self.isContainTemplate('DQ10/open_mouth.png'):
                warning = True
                
            if self.isContainTemplate('DQ10/catch_up.png'):
                print('catch up !!')
                return {
                    'continue': False,
                    'warning': False
                }
                    
            if self.isContainTemplate('DQ10/escaped.png'):
                print('escaped ...')
                return {
                    'continue': False,
                    'warning': False
                }
            
        return {
            'continue': True,
            'warning': warning
        }

    def move_natsuri(self):
        self.press(Button.R, duration=0.4, wait=1)
        self.press(Button.ZL, wait=5)
        self.press(Button.ZL, wait=1)
