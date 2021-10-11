#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

from Commands.Keys import Button, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand, StopThread


# Get watt automatically using the glitch
class shiny_egg(ImageProcPythonCommand):
    NAME = '色厳選(孵化)'

    def __init__(self, cam):
        super().__init__(cam)
        self.cam = cam
        self.cam_id = 2
        self.box = 1
        self.init_flag = True
    
        self.count = 1
        self.egg = 3
        self.hatch = 5
        self.total = 0

    def do(self):
        while(True):
            try:
                if not self.init_flag:
                    self.count = 0
                while self.count < (self.box * 6):
                    if not self.init_flag:
                        self.egg = 0
                        self.hatch = 0
                        
                    self.init_flag = False
                    while self.egg < 5 or self.hatch < 5:
                        print(f"egg: {self.egg}, hatch: {self.hatch}")
                    
                        if self.egg < 5:
                            self.press(Button.PLUS, wait=1)
                        
                            self.hatch += self.round_circle(
                                hatch=self.hatch,
                                duration=15)

                            self.press(Button.PLUS, wait=1)
                            self.reset_position()
                        
                            tmp = self.get_egg(hatch=self.hatch)
                            self.egg += tmp[0]
                            self.hatch += tmp[1]
                            
                            self.reset_position()
                        else:
                            self.press(Button.PLUS, wait=1)
                        
                            self.hatch += self.round_circle(hatch=self.hatch)

                            self.press(Button.PLUS, wait=1)
                            self.reset_position()

                    print(f"switch_eggs: {self.count}")
                    self.switch_eggs(self.count)
                    self.count += 1
                    
                self.init_flag = False            
                self.auto_release()
                self.total += 1
                print("--------------------------------")
                print(f"total: {self.total}, {30 * self.total * self.box}")
            except cv2.error as e:
                self.LINE_text(f"\n{e}\nprogram exit -1")
                raise StopThread
                
    def auto_release(self):
        direction = True
        self.press(Button.X, wait=1)
        self.press(Button.A, wait=2)
        self.press(Button.R, wait=2)

        self.press(Button.R, wait=1)
        try:
            for i in range(30):
                if self.isContainTemplate('PokemonSS/ShinyEgg/shiny_mark.png'):
                    print('shiny !!')
                    self.LINE_image(f"色違いが出ました！")
                    self.press(Button.CAPTURE, wait=0.5)
                    raise StopThread
                else:
                    if self.isContainTemplate('PokemonSS/ShinyEgg/status.png'):
                        self.release()
                        
                if i % 6 == 5 and i:
                    self.press(Direction.DOWN, wait=0.2)
                    direction = not direction
                else:
                    if direction:
                        self.press(Direction.RIGHT, wait=0.2)
                    else:
                        self.press(Direction.LEFT, wait=0.2)
                self.wait(0.5)
        except cv2.error as e:
            self.press(Button.L, wait=1)
            self.press(Button.B, wait=2)
            self.press(Button.B, wait=2)
            self.press(Button.B, wait=2)
            self.LINE_text(f"\nbreakpoint: auto_release\n{e}")
            self.cam.openCamera(self.cam_id)
            self.wait(1.0)

            self.init_flag = True
            self.count = 6
            self.egg = 0
            self.hatch = 0
            return
                
        self.press(Button.L, wait=1)
        self.press(Button.B, wait=2)
        self.press(Button.B, wait=2)
        self.press(Button.B, wait=2)
        
                
    def release(self):
        self.press(Button.A, wait=0.5)
        self.press(Direction.UP, wait=0.2)
        self.press(Direction.UP, wait=0.2)
        self.press(Button.A, wait=1)
        self.press(Direction.UP, wait=0.2)
        self.press(Button.A, wait=1.5)
        self.press(Button.A, wait=0.3)
                
    def get_egg(self, hatch):
        RETRY = 3
        EGG_NF = False
        
        tmp_hatch = self.go2bank(hatch)

        self.press(Button.A, wait=1)

        for _ in range(RETRY):
            try:
                if EGG_NF or self.isContainTemplate('PokemonSS/ShinyEgg/egg_notfound.png'):
                    EGG_NF = True
                    while not self.isContainTemplate('PokemonSS/ShinyEgg/local.png'):
                        self.press(Button.B, wait=1)
                    return 0, tmp_hatch
                else:
                    for _ in range(5):
                        self.press(Button.A, wait=1)
                    while not self.isContainTemplate('PokemonSS/ShinyEgg/local.png'):
                        self.press(Button.B, wait=1)
                    return 1, tmp_hatch
            except cv2.error:
                continue

        self.LINE_text("\nbreakpoint: get_egg\nprogram exit -1")
        raise StopThread
                
    def switch_eggs(self, count):
        # box open
        self.press(Button.X, wait=1)
        self.press(Button.A, wait=2)
        self.press(Button.R, wait=2)

        # tool change
        self.press(Button.Y, wait=0.2)
        self.press(Button.Y, wait=0.2)

        # party dd
        self.press(Direction.LEFT, wait=0.2)
        self.press(Direction.DOWN, wait=0.2)
        self.press(Button.A, wait=0.5)
        for _ in range(4):
            self.press(Direction.DOWN, wait=0.2)
        self.press(Button.A, wait=0.5)

        # box change
        self.press(Direction.RIGHT, wait=0.5)
        self.press(Button.R, wait=1)

        # put
        for _ in range(count):
            self.press(Direction.RIGHT, wait=0.2)
        self.press(Direction.UP, wait=0.2)
        self.press(Button.A, wait=0.5)

        # box change
        self.press(Button.L, wait=1)
        for _ in range(count):
            self.press(Direction.LEFT, wait=0.2)
        self.press(Button.A, wait=0.5)
        for _ in range(4):
            self.press(Direction.DOWN, wait=0.2)
        self.press(Button.A, wait=0.5)
        self.press(Direction.LEFT, wait=0.2)
        self.press(Direction.DOWN, wait=0.2)
        self.press(Button.A, wait=0.5)
        self.press(Button.B, wait=2)
        self.press(Button.B, wait=2)
        self.press(Button.B, wait=2)
        
        
    def round_circle(self, hatch, duration=100):
        tmp_hatch = 0
        
        directions = [Direction.UP]*4 + \
            [Direction.RIGHT] + \
            [[Direction.RIGHT, Direction.R_RIGHT]] * duration

        i = 0
        while i < len(directions):

            self.press(directions[i], duration=1, wait=0.1)
            try:
                if self.isContainTemplate('PokemonSS/ShinyEgg/hatch.png'):
                    tmp_hatch += self.hatch_eggs(directions[i])
                    continue
            except cv2.error as e:
                self.LINE_text(f"\nbreakpoint: round_circle\n{e}")
                self.cam.openCamera(self.cam_id)
                self.wait(1.0)
                continue
            
            if duration == 100 and tmp_hatch + hatch == 5:
                break

            i += 1

        self.wait(1)
        if self.isContainTemplate('PokemonSS/ShinyEgg/hatch.png'):
            tmp_hatch += self.hatch_eggs(directions[-1])
            
        return tmp_hatch

    def go2bank(self, hatch):
        
        tmp_hatch = 0
        
        directions = [Direction.DOWN]*2 + \
            [Direction.LEFT]

        i = 0
        while i < len(directions):

            self.press(directions[i], duration=1, wait=0.1)
            try:
                if self.isContainTemplate('PokemonSS/ShinyEgg/hatch.png'):
                    tmp_hatch += self.hatch_eggs(directions[i])
                    continue
            except cv2.error as e:
                self.LINE_text(f"\nbreakpoint: go2bank\n{e}")
                self.cam.openCamera(self.cam_id)
                self.wait(1.0)
                continue

            
            i += 1
            
        return tmp_hatch
    

    def hatch_eggs(self, direction):
        hatch = 0
        for _ in range(3):
            self.press(Button.A, wait=1)
            
        while not self.isContainTemplate('PokemonSS/ShinyEgg/local.png'):
            self.press(Button.A, wait=1)
        self.press(direction, duration=1)
        if self.isContainTemplate('PokemonSS/ShinyEgg/hatch.png'):
            hatch += self.hatch_eggs(direction)
            
        return hatch + 1
    
    def reset_position(self):
        self.press(Button.X, wait=1)
        self.press(Button.PLUS, wait=2.5)
        self.press(Button.A, wait=1)
        self.press(Button.A, wait=3)

        return None
