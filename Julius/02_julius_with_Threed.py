#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import socket
import xml.etree.ElementTree as ET
import time
from multiprocessing import Process, Value
from ctypes import c_char_p

############################################################################
#通信関連の定数
JULIUS_HOST_NAME = '127.0.0.1'    #Juliusサーバー(TCP)ホスト名
JULIUS_HOST_PORT = 10500           #Juliusサーバー(TCP)ポート番号
JULIUS_SOKET_TIMEOUT = 0.01       #Juliusサーバー(TCP)受信タイムアウトまでの時間[s]

############################################################################
# Julius（音声認識）をコントロールするクラス
class Julius_Client_Class:
    def __init__(self):
        self.process = subprocess.Popen(["bash start_julius.sh"], stdout=subprocess.PIPE, shell=True)
        self.pid = self.process.stdout.read() # juliusのプロセスIDを取得
        #print("Julius pid:"+str(self.pid))
        # TCPクライアントを作成し接続
        self.soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soket.connect((JULIUS_HOST_NAME, JULIUS_HOST_PORT))

    def Cleanup(self):
        self.process.kill()
        subprocess.call(["kill " + self.pid], shell=True) # juliusのプロセスを終了
        self.soket.close()

def Julius_loop(flag_julius_loop,Cmd_from_julius):
    print("subprocess:"+str(flag_julius_loop))
    print("subprocess:"+str(Cmd_from_julius))
    try:
        julius_client = Julius_Client_Class()
        print("Julius Initialization succeeded")
    except Exception as e:
        print(str(e))
        flag_julius_loop = False

    try:
        data = ""
        while flag_julius_loop:
            if "</RECOGOUT>\n." in data:
                # RECOGOUT要素以下をXMLとしてパース
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.", ""))
                # 言葉を判別
                for whypo in root.findall("./SHYPO/WHYPO"):
                    cmd = whypo.get("WORD")
                    if cmd == "前進":
                        print("Subprocess:"+str(cmd))
                        #Cmd_from_julius = 1
                    elif cmd == "後退":
                        print("Subprocess:"+str(cmd))
                        #Cmd_from_julius = 2
                    elif cmd == "左":
                        print("Subprocess:"+str(cmd))
                        #Cmd_from_julius = 3
                    elif cmd == "右":
                        print("Subprocess:"+str(cmd))
                        #Cmd_from_julius = 4
                    elif cmd == "止まれ":
                        print("Subprocess:"+str(cmd))
                        #Cmd_from_julius = 5
                    else:
                        print("Subprocess:"+str(cmd))
                        #Cmd_from_julius = 0
                    #print("Subprocess:"+str(Cmd_from_julius))
                data = ""
            else:
                data = data + julius_client.soket.recv(1024)
            print("Subprocess:sleep")
            time.sleep(0.5)
    except Exception as e:
        print(str(e))
    finally:
        julius_client.Cleanup()

########################################################################
#メインループ
def main_loop():
    #flag_julius_loopをスレッド間で共有する
    #flag_julius_loop = Value('d', True)
    flag_julius_loop = True
    #Cmd_from_julius = Value('d', 0)
    Cmd_from_julius = 0
    julius_process = Process(target=Julius_loop, args=(flag_julius_loop,Cmd_from_julius))
    julius_process.start()
    #julius_process.join()

    try:
        while flag_julius_loop:
            print("main_loop:"+str(Cmd_from_julius))
            time.sleep(1)
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        flag_julius_loop = False

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
