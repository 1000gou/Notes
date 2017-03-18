#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import socket
import xml.etree.ElementTree as ET
import threading
import time


############################################################################
#通信関連の定数
JULIUS_HOST_NAME = '127.0.0.1'      #Juliusサーバー(TCP)ホスト名
JULIUS_HOST_PORT = 10500            #Juliusサーバー(TCP)ポート番号
JULIUS_THREAD_SLEEP_TIME = 1        #Juliusスレッドの待ち時間
NO_COMMAND = "NoCommand"            #Juliusからコマンドがないときの文字列

############################################################################
# Julius（音声認識）をコントロールするクラス
class JuliusClientThreadClass(threading.Thread):
    def __init__(self, sleep_time):
        super(JuliusClientThreadClass, self).__init__()

        #スレッド関連のメンバ初期化
        self.lock = threading.Lock()
        self.sleep_time = sleep_time
        self.stop_event = threading.Event() #停止させるかのフラグ
        self.command = NO_COMMAND

        #Juliusの音声認識サーバーを起動する
        try:
            self.process = subprocess.Popen(["bash start_julius.sh"], stdout=subprocess.PIPE, shell=True)
            self.pid = self.process.stdout.read() # juliusのプロセスIDを取得
            print("Julius pid:"+str(self.pid))
            print("Julius server initialization succeeded")
        except Exception as e:
            print(str(e))
            print("Julius server initialization  error")
            #スレッドを停止させる
            self.stop()

        #TCPクライアントを作成し接続
        try:
            self.soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.soket.connect((JULIUS_HOST_NAME, JULIUS_HOST_PORT))
            print("Julius client initialization succeeded")
        except Exception as e:
            print(str(e))
            print("Julius client initialization  error")
            #スレッドを停止させる
            self.stop()

    def run(self):
        try:
            data = ""
            while not self.stop_event.is_set():
                if "</RECOGOUT>\n." in data:
                    #変数変更前withを使ってスレッドをロックする
                    with self.lock:
                        # RECOGOUT要素以下をXMLとしてパース
                        tmp = '<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):data.find("</RECOGOUT>")+11]
                        root = ET.fromstring(tmp)
                        # 言葉を判別
                        for whypo in root.findall("./SHYPO/WHYPO"):
                            self.command = whypo.get("WORD")
                            #print("sub_loop:"+self.command)
                        data = ""
                else:
                    data = data + self.soket.recv(1024)
                time.sleep(self.sleep_time)
        except Exception as e:
            print(str(e))
        finally:
            self.Cleanup()

    #スレッドを停止させる
    def stop(self):
        self.stop_event.set()
        self.join()             #スレッドが停止するのを待つ

    #終了準備
    def Cleanup(self):
        #Juliusの音声認識サーバーを終了する
        subprocess.call(["kill " + self.pid], shell=True)
        #TCPクライアントを終了する
        self.soket.close()
        print("JuliusClientThreadClass:cleaned up")

########################################################################
#メインループ
def main_loop():
    #Sub threadを開始する
    JuliusThread = JuliusClientThreadClass(JULIUS_THREAD_SLEEP_TIME)
    JuliusThread.start()
    time.sleep(0.1)

    try:
        while True:
            if JuliusThread.command != NO_COMMAND:
                #変数変更前withを使ってスレッドをロックする
                with JuliusThread.lock:
                    print("main_loop:"+JuliusThread.command)
                    JuliusThread.command = NO_COMMAND
            time.sleep(0.1)
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        JuliusThread.stop()

if __name__ == '__main__':
    main_loop()
    print("\nexit program\n")
