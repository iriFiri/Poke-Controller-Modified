#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread

class LegiLoop(ImageProcPythonCommand):
    NAME = 'レジループ'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam

    def do(self):
        # If camera is not opened, break
        if not self.cam.isOpened():
            print("can't work (cam.isOpend == False)")
            
        else:
            count = 1
            cam_id = 2

            while True:
                try:
                    print(f'count: {str(count)}')

                    while True:
                        try:
                            if self.isContainTemplate('encount.png'):
                                break
                        except cv2.error as e:
                            self.LINE_text(e)
                            self.LINE_text("program exit : 0")
                            # self.cam.openCamera(cam_id)
                            raise e
                        self.press(Button.A, wait=0.5)

                    shiny = True
                    for _ in range(15):
                        try:
                            if self.isContainTemplate('fight.png'):
                                shiny = False
                                break
                            self.wait(0.5)
                        except cv2.error as e:
                            self.LINE_text(e)
                            self.LINE_text("program exit : 1")
                            raise e

                    if shiny:
                        print('shiny !')
                        self.LINE_image(f"色違いが出ました！ {str(count)}回目です！")
                        self.wait(3.0)
                        self.press(Button.CAPTURE, duration=3.0, wait=0.5)
                        break
                    else:
                        print('reset !')
                        count += 1
                        self.reset_game(cam_id)

                except StopThread as t:
                    raise t
                except cv2.error as e:
                    raise e
                except Exception as e:
                    self.LINE_text(e)
                    raise e

    def reset_game(self, cam_id: int):
        self.press(Button.HOME, wait=1.0)
        self.press(Button.X, wait=0.5)
        self.press(Button.A, wait=5.0)
        self.press(Button.A, wait=1.5)
        self.press(Button.A, wait=0.5)

        while True:
            try:
                if self.isContainTemplate('OP.png', threshold=0.6):
                    break
            except cv2.error as e:
                self.LINE_text(e)
                self.cam.openCamera(cam_id)
                self.wait(1.0)
            self.wait(0.7)
            
        self.press(Button.A, wait=6.0)
        return
