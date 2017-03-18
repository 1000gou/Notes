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
