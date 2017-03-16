#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import time

def main_loop():
    flag = True
    try:
        pygame.joystick.init()
        joys = pygame.joystick.Joystick(0)
        joys.init()
        pygame.init()
        print("\npygame initialaize is succeeded")
    except Exception as e:
        print("\npygame.error")
        print(str(e))
        flag = False

    try:
        while flag:
            for e in pygame.event.get(): # イベントチェック
                if e.type == pygame.locals.JOYAXISMOTION:   #コントロールAXIS
                    left_stick = -100*joys.get_axis(1)
                    right_stick = -100*joys.get_axis(4)
                    print("reft_stick = " + str(left_stick) + ", right_stick = " + str(right_stick))
                elif e.type == pygame.locals.JOYBUTTONDOWN: #ボタンが押された
                    print str(e.button)+'番目のボタンが押された'
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
            print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
            return

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
