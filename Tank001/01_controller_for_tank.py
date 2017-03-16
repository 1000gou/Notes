#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import pygame
from pygame.locals import *

def main_loop():
    #pygameの初期化
    flag = True
    try:
        pygame.joystick.init()
        joys = pygame.joystick.Joystick(0)
        joys.init()
        pygame.init()
        print("\npygame initialaize is succeeded")
    except Exception as e:
        print("\npygame initialaize error")
        print(str(e))
        flag = False

    #ソケットの初期化
    try:
        host = '192.168.2.201'#'GApizero.local' #'127.0.0.1'
        port = 4000
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("\nsoket initialaization is succeeded")
    except Exception as e:
        print("\nsoket initialaization error")
        print(str(e))
        flag = False

    try:
        while flag:
            for e in pygame.event.get(): # イベントチェック
                print("\ngetting event")
                if e.type == pygame.locals.JOYAXISMOTION: # 7
                    left_stick = -100*joys.get_axis(1)
                    right_stick = -100*joys.get_axis(4)
                    message = "left_right_stick:"+str(left_stick)+":"+str(right_stick)
                    sock.sendto(message, (host, port))
            time.sleep(0.1)
    except KeyboardInterrupt:         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        return

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
