#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TA7291P import TA7291P_Class
import sys
import socket

def main_loop():
    flag = True
    #車輪用DCモーターコントローラーインスタンス作成
    try:
        left_motor = TA7291P_Class(Pin_ref=17, Pin_out1=18, Pin_out2=27)
        right_motor = TA7291P_Class(Pin_ref=22, Pin_out1=23, Pin_out2=24)
        print("DC motor initialaization is succeeded")
    except Exception as e:
        print("DC motor initialaization error")
        print(str(e))
        flag = False

    #ソケットの初期化
    try:
        host = 'GApizero.local' #'127.0.0.1'
        port = 4000
        bufsize = 4096
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, port))
        print("\nsoket initialaization is succeeded")
    except Exception as e:
        print("\nsoket initialaization error:")
        print(str(e))
        flag = False

    try:
        while flag:                     #ソケット受信待
            text = sock.recv(bufsize)
            cmd = text.split(":")
            if cmd[0] == 'left_right_stick':
                left_motor.SetSpeed(float(cmd[1]))
                right_motor.SetSpeed(float(cmd[2]))
                print("SetSpeed, left:"+cmd[1]+",right"+cmd[2])
    except KeyboardInterrupt:         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        return

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
