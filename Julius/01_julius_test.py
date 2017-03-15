#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import socket
import xml.etree.ElementTree as ET

############################################################################
#通信関連の定数
JULIUS_HOST_NAME = '127.0.0.1'    #Juliusサーバー(TCP)ホスト名
JULIUS_HOST_PORT = 10500           #Juliusサーバー(TCP)ポート番号
JULIUS_SOKET_TIMEOUT = 0.01       #Juliusサーバー(TCP)受信タイムアウトまでの時間[s]

############################################################################
# Julius（音声認識）をコントロールするクラス
class Julius_Client_Class:
    def __init__(self):
        #self.process = subprocess.Popen(["bash start_julius.sh"], stdout=subprocess.PIPE, shell=True)
        #self.pid = process.stdout.read() # juliusのプロセスIDを取得
        # TCPクライアントを作成し接続
        self.soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soket.connect((JULIUS_HOST_NAME, JULIUS_HOST_PORT))

    def Cleanup():
        pass
        #self.process.kill()
        #subprocess.call(["kill " + self.pid], shell=True) # juliusのプロセスを終了

########################################################################
#メインループ
def main_loop():
    try:
        julius_client = Julius_Client_Class()
        data = ""
        if "</RECOGOUT>\n." in data:
            # RECOGOUT要素以下をXMLとしてパース
            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find("<RECOGOUT>"):].replace("\n.", ""))
            # 言葉を判別
            for whypo in root.findall("./SHYPO/WHYPO"):
                if whypo.get("WORD") in colors.keys():
                    #受信した文字を表示
                    print(whypo.get("WORD"))
                data = ""
        else:
            data = data + julius_client.soket.recv(1024)
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        julius_client.Cleanup()

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
