## ラズパイで3軸加速度センサー(ADXL345)を使う
[Raspberry Pi 3 Model Bの GPIOに I2C通信方式の３軸加速度センサー ADXL345を接続する方法](http://www.neko.ne.jp/~freewing/raspberry_pi/raspberry_pi_3_i2c_accelerometer_adxl345/)および[<IoT>加速度センサの値をMQTTを使ってネット越しにやりとりする](http://xhatenen.hatenablog.com/entry/2014/12/31/005517)を参考にして作業しました。

#### 配線
ラズパイ 3.3V(1番ピン) : 　ADXL345 VDD  
ラズパイ GND : ADXL345 GND  
ラズパイ SDA1(３番ピン) : ADXL345 SDA   
ラズパイ SCL1(5番ピン) : ADXL345 SCL     

#### ラズパイ設定 (I2C通信をenableにする)
$sudo raspi-config
5 Interfacing option -> P5 I2C でI2C通信をenableにする。

$sudo i2cdetect -y 1 でどのADXL345がどのチャンネルにいるか確認する。加速度センサの場合は0x1Dにいるようです。

Pythonでセンサー値を読み取るために必要な、ツールとライブラリのインストール  
$sudo apt-get -y install python-smbus i2c-tools  

#### サンプルプログラム(01_adxl345.py)
[便利なADXL345コントロール用クラスをアップされている方](https://github.com/pimoroni/adxl345-python)がいましたので、使わせてもらうことにしました。
※adxl345.pyを以下のサンプルプログラムと同じフォルダへ保存してください。
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import adxl345
import time

def GetAccelerationG_Loop():
    #0x1Dは$sudo i2cdetect -yで確認したADXL345のアドレス
    m_adxl345 = adxl345.ADXL345(0x1D)
    try:
        while True:
            #加速度を[m/s^2]ではなく[G]で取得する。
            axes = m_adxl345.getAxes(True)
            print('x = %.2fG, y = %.2fG, z = %.2fG'%(axes['x'],axes['y'],axes['z']))
            time.sleep(1)
    except KeyboardInterrupt  :
        #Ctl+Cが押されたら終了処理を行う
        pass    #何もしなくて良い？

if __name__ == '__main__':
    GetAccelerationG_Loop()
    print("exit program")
```
