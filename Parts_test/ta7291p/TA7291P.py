#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class TA7291P_Class:
    # mPin_ref : GPIO No モーターリファレンス電圧
    #mPwm_ref : Pwmコントロール用のインスタンス
    # mPin_out1 : GPIO No モーター出力１
    # mPin_out2 : GPIO No モーター出力２

    """コンストラクタ"""
    def __init__(self, Pin_ref=23, Pin_out1=24, Pin_out2=25):
        self.mPin_ref = Pin_ref
        self.mPin_out1 = Pin_out1
        self.mPin_out2 = Pin_out2

        #Useing GPIO No.  to idetify channel
        GPIO.setmode(GPIO.BCM)

        #車輪用サーボをPWMモードにする
        GPIO.setup(self.mPin_ref, GPIO.OUT)
        self.mPwm_ref = GPIO.PWM(self.mPin_ref , 100) # set 10ms / 100 Hz
        self.mPwm_ref.start(100) #Duty比100％

        #Out1と２を出力モードにする
        GPIO.setup(self.mPin_out1, GPIO.OUT)
        GPIO.setup(self.mPin_out2, GPIO.OUT)
        self.Stop()

    """停止"""
    def Stop(self):
        GPIO.output(self.mPin_out1, GPIO.LOW)
        GPIO.output(self.mPin_out2, GPIO.LOW)

    def SetSpeed(self, speed):
        if speed > 100:
            speed = 100
        if speed < -100:
            speed = -100

        if -10< speed and speed < 10:
            self.Stop()
        elif speed > 0:
            #CW
            GPIO.output(self.mPin_out1, GPIO.HIGH)
            GPIO.output(self.mPin_out2, GPIO.LOW)
            self.mPwm_ref.start(speed)
        elif speed < 0:
            #CCW
            GPIO.output(self.mPin_out1, GPIO.LOW)
            GPIO.output(self.mPin_out2, GPIO.HIGH)
            self.mPwm_ref.start(-speed)

    """終了処理"""
    def Cleanup(self):
        #PWMを0にしてから、インプットモードにしておく
        self.Stop()
        GPIO.setup(self.mPin_ref, GPIO.IN)
        GPIO.setup(self.mPin_out1, GPIO.IN)
        GPIO.setup(self.mPin_out2, GPIO.IN)
        GPIO.cleanup()


#メイン関数（コントロール例）
if __name__ == '__main__':
    motor = TA7291P_Class(Pin_ref=23, Pin_out1=24, Pin_out2=25)
    try:
        while True:
            motor.SetSpeed(100)
            time.sleep(2)
            motor.SetSpeed(50)
            time.sleep(2)
            motor.SetSpeed(0)
            time.sleep(2)
            motor.SetSpeed(-50)
            time.sleep(2)
            motor.SetSpeed(-100)
            time.sleep(2)
            motor.SetSpeed(-50)
            time.sleep(2)
            motor.SetSpeed(0)
            time.sleep(2)
            motor.SetSpeed(50)
            time.sleep(2)
    except KeyboardInterrupt  :
        pass
    finally:
        motor.Cleanup()
        print("\nexit program")
