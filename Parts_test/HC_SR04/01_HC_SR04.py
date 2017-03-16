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
