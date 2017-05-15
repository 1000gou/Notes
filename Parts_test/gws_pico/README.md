# Servoコントロール比較
### ラズベリーパイのPWM信号の比較
1. ソフトウェアPWM(RPi):[サンプル：gws_pico.py](gws_pico.py)  
　　ジッターあり  
1. ハードウェアPWM(wiringpi, GPIO18のみ):[サンプル:gws_pico2.py](gws_pico2.py)  
　　ジッターなし  
1. セミハードウェアPWM(RPIO):[サンプル:gws_pico2.py](gws_pico2.py)   

### RPIOのインストール方法
#### Python2
$ sudo apt-get update  
$ sudo apt-get install python-dev  
$ sudo apt-get install python-setuptools  
$ git clone https://github.com/metachris/RPIO.git --branch v2 --single-branch  
$ cd RPIO  
$ sudo python setup.py install  

#### Python3  
$ sudo apt-get update  
$ sudo apt-get install python3-dev  
$ sudo apt-get install python3-setuptools  
$ git clone https://github.com/metachris/RPIO.git --branch v2 --single-branch  
$ cd RPIO  
$ sudo python3 setup.py install  

#### 動作確認
$sudo python3  
import RPIO  
ここで、「SystemError: This module can only be run on a Raspberry Pi!」というエラーが出る場合は、最新版のRPIOを以下のようにしてインストールする。  

$ git clone https://github.com/metachris/RPIO.git --branch v2 --single-branch  
$ cd RPIO  
$ sudo python setup.py install  
　　もしくは  
$ sudo python3 setup.py install  
