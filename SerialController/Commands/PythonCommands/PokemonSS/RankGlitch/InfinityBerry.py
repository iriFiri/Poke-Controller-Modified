#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


# using RankBattle glitch
# Infinity getting berries
# 無限きのみ(ランクマッチ, 画像認識任意)
class InfinityBerry(ImageProcPythonCommand):
    NAME = '無限きのみ'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam

    def do(self):
        while True:
            fight_flag = False
            # If camera is not opened, then pick 1 and timeleap
            if not self.cam.isOpened():
                self.press(Button.A, wait=0.5)
                self.press(Button.B, wait=0.5)
                self.press(Button.A, wait=0.5)  # yes

                for _ in range(0, 15):  # B loop
                    self.press(Button.B, wait=0.5)

                # Time glitch
                self.timeLeap()

            else:
                try:
                    self.press(Button.A, wait=0.7)
                    self.press(Button.B, wait=0.5)
                    self.press(Button.A, wait=0.5)  # yes

                    while True:
                        self.press(Button.A, wait=0.5)  # for press 'shake more'
                        self.press(Button.A, wait=0.5)  # just in case
                        self.press(Button.A, wait=2.0)

                        waitfell_count = 0
                        while not self.isContainTemplate('fell_message.png'):
                            print('wait fell')
                            if waitfell_count == 20:
                                break
                            if self.isContainTemplate('fight.png'):
                                fight_flag = True
                                self.press(Direction.DOWN, wait=0.2)
                                self.press(Direction.DOWN, wait=0.2)
                                self.press(Direction.DOWN, wait=0.2)
                                self.press(Button.A, wait=1.0)
                                self.press(Button.A, wait=0.5)
                                break
                            self.press(Button.B, wait=1.0)
                            waitfell_count += 1

                        if waitfell_count == 20:
                            print('wait faild')
                            self.wait(1.0)
                            break
                        if fight_flag:
                            print('fight exit')
                            self.wait(6.0)
                            break
                    
                        print('fell message!')
                        self.press(Button.A, wait=0.5)

                        # Judge continuity by tree shaking motion
                        if self.isContinue():
                            print('continue')
                            self.wait(0.5)
                            continue
                        else:
                            print('not continue')
                            self.press(Button.B, wait=3.0)
                            break
                        
                    while self.isContainTemplate('textbox.png'):
                        print('close textbox')
                        self.press(Button.B, wait=1.0)

                    # Time glitch
                    self.timeLeap()
                    
                except StopThread as t:
                    raise t
                except Exception as e:
                    self.LINE_text(e)
                    raise e

    def isContinue(self, check_interval=0.1, check_duration=2):
        time = 0
        zero_cnt = 0
        height_half = int(self.camera.capture_size[1] / 2)

        frame1 = cv2.cvtColor(self.camera.readFrame()[0:height_half - 1, :], cv2.COLOR_BGR2GRAY)
        self.wait(check_interval / 3)
        frame2 = cv2.cvtColor(self.camera.readFrame()[0:height_half - 1, :], cv2.COLOR_BGR2GRAY)
        self.wait(check_interval / 3)
        frame3 = cv2.cvtColor(self.camera.readFrame()[0:height_half - 1, :], cv2.COLOR_BGR2GRAY)

        while time < check_duration:
            mask = self.getInterframeDiff(frame1, frame2, frame3, 15)
            zero_cnt += cv2.countNonZero(mask)

            frame1 = frame2
            frame2 = frame3
            self.wait(check_interval)
            frame3 = cv2.cvtColor(self.camera.readFrame()[0:height_half - 1, :], cv2.COLOR_BGR2GRAY)

            time += check_interval

        print('diff cnt: ' + str(zero_cnt))

        # zero count threshold is heuristic value... weather: sunny
        return True if zero_cnt < 10000 else False
