## ラズパイでLED点灯

#### ターミナルからLEDを点灯
$ sudo su -   
$ echo "4" > /sys/class/gpio/export  
$ echo "out" > /sys/class/gpio/gpio4/direction    
$ (点灯)# echo "1" > /sys/class/gpio/gpio4/value  
$ (消灯) # echo "0" > /sys/class/gpio/gpio4/value  
$ exit

#### PythonからLEDの制御  
$ python  
\>> import RPi.GPIO as GPIO  
\>> GPIO.setmode(GPIO.BCM)  
\>> GPIO.setup(4,GPIO.OUT)  
\#点灯  
\>> GPIO.output(4,GPIO.HIGH)  
\#消灯  
\>> GPIO.output(4,GPIO.LOW)  
\>> exit()

#### LEDを点滅させるPythonプログラムのサンプルコード
```Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

def led_on_off():
    LED = 26 #GPIO Number
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)

    #Main loop
    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(LED, GPIO.LOW)
            sleep(0.5)

    #When Ctl +C pushed
    except KeyboardInterrupt :
        pass  #Noting to do

    #clean up GPIO
    GPIO.cleanup()

if __name__ == '__main__':
    led_on_off()
```
