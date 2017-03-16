#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class GWS_S35_STD_Class:
    # mPin : GPIO No (PWM)
    # mPwm : Pwmコントロール用のインスタンス
    # mReversal (1:CW/CCWそのまま、−１:CW/CCW反転)

    """コンストラクタ"""
    def __init__(self, Pin, Reversal):
        self.mPin = Pin
        self.mReversal = Reversal

        #Useing GPIO No.  to idetify channel
        GPIO.setmode(GPIO.BCM)

        #車輪用GPIOをPWMモードにする
        GPIO.setup(self.mPin, GPIO.OUT)
        self.mPwm = GPIO.PWM(self.mPin , 500) # set 2.0ms / 500 Hz
        self.Stop()

    """停止"""
    def Stop(self):
        self.mPwm.start(0)

    """速度セット"""
    def SetSpeed(self, speed):
        if speed > 100:
            speed = 100
        elif speed < -100:
            speed = -100
        elif -10 < speed and speed < 10:
            self.Stop()
        else:
            #Duty ratio = ６０％〜９０％（1.2ms〜1.8ms)
            duty = (self.mReversal*speed+100)/200*30+60
            self.mPwm.start(duty)

    """終了処理"""
    def Cleanup(self):
        #PWMを0にしてから、インプットモードにしておく
        self.Stop()
        GPIO.setup(self.mPin, GPIO.IN)
        GPIO.cleanup()

"""GWS_S35_STDのコントロール例"""
if __name__ == '__main__':
    Servo = GWS_S35_STD_Class(Pin=17,Reversal=1)

    try:
        while True:
            Servo.SetSpeed(100)
            time.sleep(3)
            Servo.SetSpeed(0)
            time.sleep(3)
            Servo.SetSpeed(-100)
            time.sleep(3)
            Servo.SetSpeed(0)
            time.sleep(3)
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        Servo.Cleanup()
        print("\nexit program")
