## ラズパイで超音波距離計（HC-SR04）を使う
[超音波距離センサ(HC-SR04)を使う](http://make.bcde.jp/raspberry-pi/%E8%B6%85%E9%9F%B3%E6%B3%A2%E8%B7%9D%E9%9B%A2%E3%82%BB%E3%83%B3%E3%82%B5hc-sr04%E3%82%92%E4%BD%BF%E3%81%86/)および[Raspberry Piに超音波距離計”HC-SR04”つけてみた](http://arkouji.cocolog-nifty.com/blog/2014/05/raspberry-pihc-.html)を参考にして作業しました。

#### 配線
ラズパイ 5V : HC-SR04　VCC  
ラズパイ GND : HC-SR04 GND  
ラズパイ　GPIO17 : HC-SR04 Trig  
ラズパイ　GPIO18 : HC-SR04 Echo    
※本当はHC-SR04がECHO端子から出力する電圧は5V、Raspberry Piの入出力端子でありGPIOは、3.3V用なので、分圧をとるために抵抗を使用する必要があるそうですが、今回はすべて直結しました。

#### サンプルプログラム（01_HC_SR04.py）
```Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

PIN_TRIG = 17  #GPIO No TRIG
PIN_ECHO = 27  #GPIO No ECHO

"""イニシャライズ"""
def setup():
    #Useing GPIO No.  to idetify channel
    GPIO.setmode(GPIO.BCM)

    #TRIGを出力モードにする
    GPIO.setup(PIN_TRIG, GPIO.OUT)
    GPIO.output(PIN_TRIG, GPIO.LOW)
    #ECHOを入力モードにする
    GPIO.setup(PIN_ECHO, GPIO.IN)


"""終了処理"""
def destroy():
    #インプットモードにしてからクリーンナップしておく
    GPIO.setup(PIN_TRIG, GPIO.IN)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.cleanup()

"""GWS_S35_STDのコントロール例"""
def GetDistanceLoop():
    #イニシャライズ
    setup()
    try:
        while True:
            #なぜかよくわからないがセンサー取得前に少し待つ（必要？）
            time.sleep(0.5)
            #TRIGを0.1us間HIGHにする
            GPIO.output(PIN_TRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(PIN_TRIG, GPIO.LOW)
            #超音波が跳ね返ってくるまでの時間を計測する
            while GPIO.input(PIN_ECHO)==0:
                signaloff = time.time()
            while GPIO.input(PIN_ECHO)==1:
                signalon = time.time()
            timepassed = signalon - signaloff
            #音速から時間を距離に変換する
            distance = timepassed * 17000
            #距離を出力する
            print('%.0f' % distance)
    except KeyboardInterrupt  :
        #Ctl+Cが押されたら終了処理を行う
        destroy()

if __name__ == '__main__':
    GetDistanceLoop()
    print("\nexit program")
```
