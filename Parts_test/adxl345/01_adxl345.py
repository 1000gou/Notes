#!/usr/bin/env python
# -*- coding: utf-8 -*-
import adxl345
import time

def GetAccelerationG_Loop():
    #0x1Dは$sudo i2cdetect -yで確認したADXL345のアドレス
    m_adxl345 = adxl345.ADXL345(0x1D)
    try:
        while True:
            #加速度を[m/s^2]ではなく[G]で取得する。
            axes = m_adxl345.getAxes(True)
            print('x = %.2fG, y = %.2fG, z = %.2fG'%(axes['x'],axes['y'],axes['z']))
            time.sleep(1)
    except KeyboardInterrupt  :
        #Ctl+Cが押されたら終了処理を行う
        pass    #何もしなくて良い？

if __name__ == '__main__':
    GetAccelerationG_Loop()
    print("exit program")
