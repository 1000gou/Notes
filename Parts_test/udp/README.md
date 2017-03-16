## PythonでUDP通信
#### サンプルプログラム受信側(01_udp_receive.py)
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket

def main_loop():
    #メインループ用フラグ
    flag = True

    #ソケットの初期化
    try:
        host = '127.0.0.1'
        port = 4000
        bufsize = 4096
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, port))
        #ソケット作成成功したかどうかのフラグ
        flag_sock = True
        print("\nsoket initialaization is succeeded")
    except Exception as e:
        print("\nsoket initialaization error:")
        print(str(e))
        flag = False

    #メインループ
    try:
        while flag:                     #ソケット受信待
            text = sock.recv(bufsize)
            if text == 'forward':
                print('1')
            elif text == 'backward':
                print('2')
            elif text == 'turn_right':
                print('3')
            elif text == 'turn_left':
                print('4')
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        if flag_sock:
            sock.close()
        return

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
```

#### サンプルプログラム送信側(01_udp_send.py)
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time

def main_loop():
    #メインループ用フラグ
    flag = True


    #ソケットの初期化
    try:
        host = '127.0.0.1'
        port = 4000
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #ソケット作成成功したかどうかのフラグ
        flag_sock = True
        print("\nsoket initialaization is succeeded")
    except Exception as e:
        print("\nsoket initialaization error")
        print(str(e))
        flag = False
        flag_sock = false

    #メインループ
    try:
        while True:
            message = 'forward'
            print(message)
            sock.sendto(message, (host, port))
            time.sleep(1)
            message = 'backward'
            print(message)
            sock.sendto(message, (host, port))
            time.sleep(1)
            message = 'turn_right'
            print(message)
            sock.sendto(message, (host, port))
            time.sleep(1)
            message = 'turn_left'
            print(message)
            sock.sendto(message, (host, port))
            time.sleep(1)
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        if flag_sock:
            sock.close()
        return

if __name__ == '__main__':
    main_loop()
    print("\nexit program")
```
