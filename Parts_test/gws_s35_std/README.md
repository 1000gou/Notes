## ラズパイでローテーションサーボ（GWS S35 STD）を使う
※GWS S35 STDはPWM信号によって、サーボの角度をコントロールするのではなく、PWM信号によってサーボの回転速度をコントロールするローテーションサーボと呼ばれるサーボです。今回は、このサーボを２つ使って、Sumobot Jrをコントロールしました。

#### 配線と制御信号
ラズパイ 5V : GWS S35 STD 電源（赤）  
ラズパイ GND : GWS S35 STD 電源（黒）  
ラズパイ　GPIO12 : GWS S35 STD PWM信号（白）

制御信号
PWM周期 ： 2.0ms (500Hz)  
CW : Duty比50％ (1.5ms)  
※Duty比に対して速度はほぼ一定のようだったのでサンプルプログラムではDuty比60％を使用
CCW : Duty比100％ (2.0ms)  
※Duty比に対して速度はほぼ一定のようだったのでサンプルプログラムではDuty比90％を使用  

#### GWS S35 STDを用いた作動Sumobot Jrコントロールのサンプルプログラム（01_GWS_S35_STD.py）
```Python
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
    Servo = GWS_S35_STD_Class(12,1)

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
```
