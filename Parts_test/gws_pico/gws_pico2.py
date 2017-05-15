#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi as wiringpi
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

        #initialize wiringpi
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.mPin, wiringpi.GPIO.PWM_OUTPUT) # pwm only works on GPIO port 18
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS) # pwmSetModeの変更は周波数を固定にする設定である。デフォルトのwiringpiではDUTY比を変更すると周波数も変更されてしまう。

        # clock = 19.2*10^6[Hz]/50[Hz]*1024=375
        wiringpi.pwmSetClock(375) #50Hz:20ms

    """位置セット"""
    def SetPos(self,pos):
        #Duty ratio = 4.5%〜10.5% : 0.9ms〜2.1ms : 0 ～ 120deg :0 ～　1024
        duty = int(((10.5-4.5)/120*pos+4.5+self.mZeroOffsetDuty)*1024/100)
        wiringpi.pwmWrite(self.mPin, duty)


    """終了処理"""
    def Cleanup(self):
        #サーボを10degにセットしてから、インプットモードにしておく
        self.SetPos(60)
        time.sleep(1)
        wiringpi.pinMode(self.mPin, wiringpi.GPIO.INPUT)


"""コントロール例"""
if __name__ == '__main__':
    #Useing GPIO No.  to idetify channel
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
        print("\nexit program")
