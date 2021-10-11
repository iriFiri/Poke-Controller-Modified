#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Hat, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


# Get watt automatically using the glitch
class test_hat(ImageProcPythonCommand):
    NAME = '[test] hat'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.cam_id = 2

    def do(self):
        self.test_code()

    def test_code(self):        
        self.press(Button.A, duration=1, wait=1)
        print("------------------")
        self.press(Button.B, duration=1, wait=1)
        print("------------------")
        self.press(Button.X, duration=1, wait=1)
        print("------------------")
        self.press(Button.Y, duration=1, wait=1)
        print("------------------")
        self.press(Hat.TOP, duration=1, wait=1)
        print("------------------")
        self.press(Hat.LEFT, duration=1, wait=1)
        print("------------------")
        self.press(Hat.BTM, duration=1, wait=1)
        print("------------------")
        self.press(Hat.RIGHT, duration=1, wait=1)
        print("------------------")
        
        return
