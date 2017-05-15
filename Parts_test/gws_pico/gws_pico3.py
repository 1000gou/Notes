#!/usr/bin/env python
# -*- coding: utf-8 -*-
from RPIO import PWM
import time

#SG92Rをコントロールするための
class SwsPico_Class:
    # mPin : GPIO Number (PWM)
    # mPwm : Pwmコントロール用のインスタンス
    # mZero_offset_duty :

    """コンストラクタ"""
    def __init__(self, Pin, ZeroOffsetDuty):
        self.mPin = Pin
        self.mZeroOffsetDuty = ZeroOffsetDuty

        #initialize RPIO
        self.mServo = PWM.Servo() #50Hz:20ms

    """位置セット"""
    def SetPos(self,pos):
        #Duty ratio = 4.5%〜10.5% : 0.9ms〜2.1ms : 0 ～ 120deg :
        OnTime = (2100-900)/120*pos+900+self.mZeroOffsetDuty
        self.mServo.set_servo(self.mPin, OnTime)


    """終了処理"""
    def Cleanup(self):
        self.mServo.stop_servo(self.mPin)

"""コントロール例"""
if __name__ == '__main__':
    #Useing GPIO No.  to idetify channel
    Servo = SwsPico_Class(Pin=17,ZeroOffsetDuty=-120)

    try:
        while True:
            Servo.SetPos(10)
            time.sleep(1)
            Servo.SetPos(60)
            time.sleep(1)
            Servo.SetPos(110)
            time.sleep(1)
            Servo.SetPos(60)
            time.sleep(1)
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo.Cleanup()
        print("\nexit program")
