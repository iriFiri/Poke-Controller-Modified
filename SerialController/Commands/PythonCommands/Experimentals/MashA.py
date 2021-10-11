#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Hat, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


# Get watt automatically using the glitch
class test_catch(ImageProcPythonCommand):
    NAME = '[test] catch'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.cam_id = 2

    def do(self):
        self.test_code()

    def test_code(self):
        while True:
            self.press(Button.A)
            self.press(Button.A)
            self.press(Direction.LEFT)
        return
