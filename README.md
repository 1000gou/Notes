# メモ
※ここには、あまりまとまっていないアイデアやメモなどを保存しています。


### Items
1. [人類の進歩が分かる年表](History.md)  
1. [Github関連メモ](GitHub.md)
1. [Fusion360関連メモ](Fusion360.md)
1. [Drone関連メモ](Drone.md)
1. [KHR-3HV関連メモ](KHR-3HV)
1. [エクセルマクロ](Excel_Macro)
1. [ラズパイでの電子部品の使い方の勉強と実験結果](Parts_test/README.md)
  1. [ラズパイでLED点灯](Parts_test/LED/README.md)
  1. [ラズパイでローテーションサーボ（GWS S35 STD）を使う](Parts_test/gws_s35_std/README.md)
  1. [ラズパイで超音波距離計（HC-SR04）を使う](Parts_test/HC_SR04/README.md)
  1. [ラズパイで3軸加速度センサー(ADXL345)を使う](Parts_test/adxl345/README.md)
  1. [ラズパイでDCモータードライバー(TA7291P)を使う](Parts_test/ta7291p/README.md)
  1. [PythonでJoystickを使う](Parts_test/joystick/README.md)
  1. [PythonでのUDP通信](Parts_test/udp/README.md)
1. [Sumobot Jrの自律化へ向けたROSの勉強(Ubuntu 14.04 LTS + ROS Indigo)](ROS/README.md)
  1. [ROSのインストールと環境設定](ROS/ros_install.md)  
  1. [ROSコマンド](ROS/ros_command.md)  
  1. [Hello World with ROS + Python](ROS/src/ros_start/README.md)
  1. [Gazebo (シミュレーター)とRviz（可視化ツール）を使ってみる](ROS/gazebo_Rviz.md)
  1. [Joystickを使ってみる](ROS/Joystick.md)
1. [ROSのRaspberry_piへのインストールと環境設定 その1（途中で挫折）](ROS_Raspi/ros_install_in_rasbian_rasbian_jessie.md)  
    ※『Raspberry Pi3 + rasbian + ROS indigo』という環境の構築を目指しましたが、ROS初心者のためなんども解決困難なエラーに見まわれそうだという結論に達しました。いろいろ調べたところ『Raspberry Pi2 + Ubuntu 14.04 LTS + ROS indigo』 もしくは 『Raspberry Pi3 + ubuntu 16.04 LTS + ROS ROS Kinetic Kame』の環境構築を目指すのが良いようです。  


### Notes
1. RaspberryPiでのソフトのインストール時は、Python2とPtyhon3の環境が混在してしまう。特にpipを使うときは要注意。pip2やpip3のように明示的に使い分けたほうが良い。  
1. SLAM(Simultaneous Localization and Mapping) ロボットの位置推定と環境マップの作成がROSでできるみたい。
1. Visual Odometry ロボット自身の移動量を計測する手法全般のこと([参考情報](https://medium.com/@NegativeMind/opencv%E3%81%A7%E3%82%AB%E3%83%A1%E3%83%A9%E7%94%BB%E5%83%8F%E3%81%8B%E3%82%89%E8%87%AA%E5%B7%B1%E4%BD%8D%E7%BD%AE%E8%AA%8D%E8%AD%98-visual-odometry-7a983cf64127#.2v97o6ir2))。SLAMはVisual Odometry + Maping?
1. Sumobotに用いたサーボは、GWS S35 STD。20ms(50Hz)の信号のDuty比で速度を制御(1.5ms停止、1.0ms～2.0ms（どっちがCW？))。
1. タクトスイッチの回路作成時は抵抗２ケ必要（GPIOがOutになっていてもショートしないようにするため) →[情報元](https://tool-lab.com/make/raspberrypi-startup-22/)
1. TensorFlow用の物体認識の学習済みモデルがネットに落ちているらしい。
1. RoboWare:ROS用のIDE
1. Cartographer：オープンソースのSLAMライブラリ by google  
<<<<<<< Updated upstream
1. SLAMの応用例：[Google Tango](https://get.google.com/tango/), [ルンバ980](http://trendy.nikkeibp.co.jp/article/pickup/20151002/1066839/?P=5&rt=nocnt)  
1. LIDER(ライダー)：LADAR(レーダー)よりも短い波長の電磁波を用いることでより緻密に計測ができる物かな？[この動画](https://www.youtube.com/watch?v=gCpCGkwwy8I)を見ると結構面白そう。ただし、[値段が高い](http://www.robotshop.com/jp/ja/lidar.html)。  

### 買いたい電子工作部品
=======
### 買いたい物
>>>>>>> Stashed changes
1. DCモーター用のバイパスコンデンサ（セラコン 0.1μＦでよいのかな？）
1. ESP-WROOM-02 開発ボード ([これ](http://goji2100.com/blog/?p=534#comment-13214)を作りたい)
1. Wii リモコン
1. 作動角１８０°のサーボ(SG-90：400円✕３つぐらい？ほしい)
1. 作動角360°のサーボ

### 家にある電子工作部品
1. タミヤ　楽しい工作シリーズ　No.170
1. RaspberryPi 3 ModelB(1個、Sumobot Jrに使用)
1. RaspberryPi Zero（１個、タンクロボットに使用）
1. ローテーションサーボ GWS S35 STD（2個、[使ってみた](Parts_test/Rotation_servo/README.md))  
1. 超音波距離センサー HC-SR04(2個、[使ってみた](Parts_test/HC_SR04/README.md))
1. 3軸加速度センサーモジュール((I2C or SPI) ADXL345 1個,[使ってみた](Parts_test/adxl345/README.md))  
1. モータードライバ TA7291P(4個、[使ってみた](Parts_test/ta7291p/README.md))
1. 抵抗（330Ω、1kΩ、10kΩ　各１００個）
1. 導線（信号用外径１．２mmと電源用外径？mm）
1. 熱収縮チューブ
1. USBシリアル変換ケーブル(ロジックレベル 3.3V)　Adafruit 954B  
1. 発光ダイオード（黄HT204YD 3個、緑HT204GD 3個、赤HT204SRD 3個）
1. ポテンショメーター RK09K1130A70 1個
1. 電池ボックス　単３✕１（まだ使っていない）
1. 電池ボックス　単３✕２直列（エネループで2.4V、タミヤ工作シリーズの単３化に使用　No.170に使用）
1. 電池ボックス　単３✕4（エネループで4.8V,まだ使っていない）
1. 電池ボックス　単３✕８直列（ラズパイ３電源に使用してみた）
1. 100円ショップで買ったUSB電源 5V,2.1A (エネループと組み合わせてRaspberryPi3が動いた。)

### 家にあるACアダプタ
1. 出力　19V 3.16A(もともとSharpのPC用だったがPCが壊れたので電子工作に使用可)
1. 出力　19V 2.15A(Acer PC用)
1. 出力　16V 4.06A(Let's Note用)
1. 出力　12.6V 0.6A(KHRのバッテリー充電用)
1. 出力　12V 1.6A(電子工作用)
1. 出力　10.7V 3.0A(KHR-3HV用に変換コネクタ作成済み)
1. 出力　8.7V 1.7A(カメラのバッテリ用だったが使ってないので改造可)　
1. 出力　5V 3.0A(ラズパイ用)
1. 出力　５V １．0A（電子工作用）

### 図書館で借りたことのある本s
1. 『詳説 ROSロボットプログラミング』([無料PDF](http://irvs.github.io/rosbook_jp/))・・・サンプルプログラムはC++  
1. 『ROSではじめるロボットプログラミング』(ISBN978-4-7775-1901-9)・・・サンプルプログラムはPythonメイン（C++の章もある）  
1. 『ROSプログラミング』(ISBN978-4-627-85341-6)・・・サンプルプログラムはC++  
