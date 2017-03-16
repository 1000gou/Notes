# Sumobot Jrの自律化へ向けたROSの勉強(Ubuntu 14.04 LTS + ROS Indigo)

環境地図の作成と位置決定([こんな感じのこと](https://www.youtube.com/watch?v=_uhOLz47t7E))をSumobot Jrでおこないたいです。このような技術はSLAM(Simultaneous Localization and Mapping)というそうですが、ROSを導入することにより実現が可能なようです。しかし、いきなりラズパイ上でROSの使い方を学ぶのは難易度がたかそうなので、PCにUbuntu 14.04 LTS + ROS IndigoをインストールしてROSの使い方を学ぶことにしました。

### Items　
1. [Ubuntuのセッティング](../Ubuntu_Setting.md)  
1. [ROSのインストールと環境設定](ros_install.md)  
1. [ROSコマンド](ros_command.md)  
1. [Hello World with ROS + Python](src/ros_start/README.md)
1. [Gazebo (シミュレーター)とRviz（可視化ツール）を使ってみる](gazebo_Rviz.md)
1. [Joystickを使ってみる](Joystick.md)

###　トラブルシュート
1. トラブル：  
RvizとGazeboの画面が真っ暗で何も表示されない。  
解決法：  
どうやら、OpenGLのエラーらしい([情報元](http://demura.net/lecture/12406.html)）。
以下のコマンドを./bashrcの最後に追加する。
```$export LIBGL_ALWAYS_SOFTWARE=1```
