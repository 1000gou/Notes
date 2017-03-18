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
