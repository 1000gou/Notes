# iBeacon関連のメモ
とりあえず、[こちら](http://ohwhsmm7.blog28.fc2.com/blog-entry-432.html)を読んで勉強しています。


### Ubuntuをペリフェラル（発信源）にする
$ sudo apt-get update  
必要なライブラリのダウンロード  
$ sudo apt-get install libbluetooth-dev  

ペリフェラル（発信源）として動作させる bluez-ibeacon を取得しmakeする
$ sudo git clone https://github.com/carsonmcdonald/bluez-ibeacon.git
$ cd bluez-ibeacon/bluez-beacon/
$ sudo make

ibeaconを実行する
$ sudo ./ibeacon 200 e2c56db5dffb48d2b060d0f5a71096e0 0 0 -20

オプションは以下、
$ sudo ./ibeacon advertisement_time UUID major_number minor number RSSI_calibration  

advertisement_time[ms]:  
UUID:  
major_number:   
minor_number:  
RSSI_cali[dB]:受信したときに、電波の強さから距離算出のためにキャリブレーションが必要になります。  
計算式:  
d[m] = 10 ^ ((TxPower - RSSI) / 20)

### Androidに受信用のアプリをインストールする
[iBeacon Detector](https://play.google.com/store/apps/details?id=youten.redo.ble.ibeacondetector&hl=ja)をアンドロイドにインストールして確認したところUbuntuのUUIDからiBeaconが出ていることがわかりました。
