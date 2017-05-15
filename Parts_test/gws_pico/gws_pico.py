#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

#SG92Rをコントロールするための
class SwsPico_Class:
    # mPin : GPIO Number (PWM)
    # mPwm : Pwmコントロール用のインスタンス
    # m_Zero_offset_duty :

    """コンストラクタ"""
    def __init__(self, Pin, ZeroOffsetDuty):
        self.mPin = Pin
        self.m_ZeroOffsetDuty = ZeroOffsetDuty

        #GPIOをPWMモードにする
        GPIO.setup(self.mPin, GPIO.OUT)
        self.mPwm = GPIO.PWM(self.mPin , 50) # set 20ms / 50 Hz

    """位置セット"""
    def SetPos(self,pos):
        #Duty ratio = 4.5%〜10.5% : 0.9ms〜2.1ms : 0 ～ 120deg
        duty = (10.5-4.5)/120*pos+4.5+self.m_ZeroOffsetDuty
        self.mPwm.start(duty)


    """終了処理"""
    def Cleanup(self):
        #サーボを10degにセットしてから、インプットモードにしておく
        self.SetPos(60)
        time.sleep(1)
        GPIO.setup(self.mPin, GPIO.IN)

"""コントロール例"""
if __name__ == '__main__':
    #Useing GPIO No.  to idetify channel
    GPIO.setmode(GPIO.BCM)
    Servo = SwsPico_Class(Pin=18,ZeroOffsetDuty=0)

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
        GPIO.cleanup()
        print("\nexit program")
