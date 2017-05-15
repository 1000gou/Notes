#!/usr/bin/env python
# -*- coding: utf-8 -*-

from RPIO import PWM
import time

#SG92Rをコントロールするための
class SG92R_Class:
    # mPin : GPIO Number (PWM)
    # mPwm : Pwmコントロール用のインスタンス
    # m_Zero_offset_duty :

    """コンストラクタ"""
    def __init__(self, Pin, ZeroOffsetDuty):
        self.mPin = Pin
        self.mZeroOffsetDuty = ZeroOffsetDuty

        #initialize RPIO
        self.mServo = PWM.Servo() #50Hz:20ms

    """位置セット"""
    def SetPos(self,pos):
        #Duty ratio = 2.5%〜12.0% : 0.5ms〜2.4ms : 0 ～ 180deg
        OnTime = (2400-500)/180*pos+500+self.mZeroOffsetDuty
        self.mServo.set_servo(self.mPin, OnTime)


    """終了処理"""
    def Cleanup(self):
        self.mServo.stop_servo(self.mPin)

"""コントロール例"""
if __name__ == '__main__':
    Servo = SG92R_Class(Pin=17,ZeroOffsetDuty=200)
    Servo2 = SG92R_Class(Pin=27,ZeroOffsetDuty=-200)
    try:
        while True:
            Servo.SetPos(90)
            Servo2.SetPos(90)
            """
            i_min = 80
            i_max = 100
            for i in range(i_min ,i_max):
                Servo.SetPos(i)
                Servo2.SetPos(i)
                Servo3.SetPos(i)
                time.sleep(0.05)
            """
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo.Cleanup()
        Servo2.Cleanup()
        Servo3.Cleanup()
        print("\nexit program")
