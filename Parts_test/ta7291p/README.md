## ラズパイでDCモータードライバー(TA7291P)を使う
[Raspberry pi 2 + モータードライバTA7291P](http://windvoice.hatenablog.jp/entry/2016/01/16/220541)や[白黒なのにカラーに見える!? モーターを制御して「ベンハムのコマ」を作ろう！ (1/3)]http://monoist.atmarkit.co.jp/mn/articles/1401/07/news003.html
を参考にして作業しました。  

#### 配線
ラズパイ 5V : ＴＡ７２91P VCC(IC電源、7番)  
ラズパイ GND : ＴＡ７２91P GND(1番)    
ラズパイ GPIO23 : ＴＡ７２９１Ｐ VREF(PWMで速度が変えられる？、４番)     
ラズパイ GPIO24 : ＴＡ７２９１Ｐ　IN1(5番)  
ラズパイ GPIO25 : TA7291P　IN２（６番）     
モーター電源（電池の＋） : ＴＡ７２91P モーター用電源(IC電源、8番)  
モーター ： ＴＡ７２91P OUT1(モーター用出力、2番)  
モーター ： ＴＡ７２91P OUT2(モーター用出力、10番)  

#### サンプルプログラム(TAP7291.py)
```python
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

        if speed == 0 :
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
```
