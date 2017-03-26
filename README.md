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


### 図書館で借りたことのある本
1. 『詳説 ROSロボットプログラミング』([無料PDF](http://irvs.github.io/rosbook_jp/))・・・サンプルプログラムはC++  
1. 『ROSではじめるロボットプログラミング』(ISBN978-4-7775-1901-9)・・・サンプルプログラムはPythonメイン（C++の章もある）  
1. 『ROSプログラミング』(ISBN978-4-627-85341-6)・・・サンプルプログラムはC++  
