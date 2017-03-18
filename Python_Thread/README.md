# Pythonでマルチスレッドプログラミング
※実験環境　Ubuntu 14.04 LTS + Python 2.7.6

### 参考にした情報
1. [Pythonでマルチスレッド処理](http://qiita.com/konnyakmannan/items/2f0e3f00137db10f56a7)  
1. [実行中のスレッドに対し外から操作をする](http://qiita.com/xeno1991/items/b207d55a413664513e5f)


### Threadクラスを用いた簡単なプログラム例([01_Thread.py](01_Thread.py))  
```Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

########################################################
#Sub Thread クラス
class SubThreadClass(threading.Thread):
    def __init__(self, sleep_time):
        super(SubThreadClass, self).__init__()
        self.sleep_time = sleep_time

    def run(self):
        print("Sub:Start")
        time.sleep(self.sleep_time )
        print("Sub:End")

########################################################
#メイン関数
if __name__ == '__main__':
    #Sub threadの中で3秒待
    myThread = SubThreadClass(sleep_time=3)
    myThread.start()

    #メインスレッドは待ち時間0.1+0.1=0.2sなので、Sub Threadよりも先に終了する
    time.sleep(0.1)
    print("Main:Start")
    time.sleep(0.1)
    print("Main:End")
```

実行結果
```
Sub:Start
Main:Start
Main:End    ←　待ち時間が短いのでメインスレッドが先に終了する
Sub:End
```  

### Threadクラスを用いた簡単なプログラム例 ([02_Thread.py](02_Thread.py))
※共有する変数を変更する前にwithを使ってロック  
※メインスレッド終了前にサブスレッドを終了させる
```Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

########################################################
#Sub Thread クラス
class SubThreadClass(threading.Thread):
    def __init__(self, sleep_time):
        super(SubThreadClass, self).__init__()
        self.lock = threading.Lock()

        #変数変更前にスレッドをロックする
        self.lock.acquire()
        try:
            self.sleep_time = sleep_time
            self.stop_event = threading.Event() #停止させるかのフラグ
            self.i = 0
        finally:
            #変数変更後アンロックする
            self.lock.release()

    def run(self):
        try:
            while not self.stop_event.is_set():
                #変数変更前withを使ってスレッドをロックする
                with self.lock:
                    self.i = self.i+1
                    print("Sub:"+str(self.i))
                time.sleep(self.sleep_time)
        except Exception as e:
            print(str(e))
        finally:
            print("\nSub:Stopped")

    #スレッドを停止させる
    def stop(self):
        self.stop_event.set()
        self.join()             #スレッドが停止するのを待つ

########################################################
#メインループ
def main_loop():
    #Sub threadを開始する
    myThread = SubThreadClass(sleep_time=1)
    myThread.start()
    time.sleep(0.1)

    try:
        i = 0
        while True:
            i = i+1
            print("Main:"+str(i))
            #変数変更前withを使ってスレッドをロックする
            with myThread.lock:
                print("Sub_from_Main:"+str(myThread.i))
                myThread.i = 0
                print("Sub_from_Main:"+str(myThread.i))
            time.sleep(2)
    except KeyboardInterrupt  :  #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        myThread.stop()   #サブスレッドを終了する

########################################################
#メイン関数
if __name__ == '__main__':
    main_loop()
    print("\nexit program")
```
実行結果  
```
Sub:1
Main:1
Sub_from_Main:1
Sub:1
Sub:2
Main:2
Sub_from_Main:2
Sub:1
Sub:2
Main:3
Sub_from_Main:2
Sub:1
Sub:2
Main:4
Sub_from_Main:2
^C
Ctl+C

Sub:Stopped

exit program
goichi@gaubutwo:Python_Thread$ python 02_Thread.py
Sub:1
Main:1
Sub_from_Main:1
Sub_from_Main:0
Sub:1
Sub:2
Main:2
Sub_from_Main:2
Sub_from_Main:0←Mainループでサブループのカウンターを０にリセットしている
Sub:1
Sub:2
Main:3
Sub_from_Main:2
Sub_from_Main:0
Sub:1
^C
Ctl+C

Sub:Stopped←メインループ終了前にサブスレッドを終了させている。

exit program
goichi@gaubutwo:Python_Thread$
```
