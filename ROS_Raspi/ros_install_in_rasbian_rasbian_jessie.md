## ROSのRaspberry_piへのインストールと環境設定 その1（途中で挫折）


### chronyをインストールして時刻を正確に設定する
$sudo apt-get install chrony
$sudo apt-get install -y ntpdate  
$sudo ntpdate -q ntp.ubuntu.com

### ROSのインストールの準備
※ここからは[ここ](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Indigo%20on%20Raspberry%20Pi)と[ここ](http://ishi.main.jp/ros/ros_rpi3.html)参考として作業した。  

ROSリポジトリアドレスを追加  
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu jessie main" > /etc/apt/sources.list.d/ros-latest.list'  

公開鍵を追加する   
$wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add -  

依存するライブラリのインストール
$ sudo apt-get update  
$ sudo apt-get upgrade   
$ sudo apt-get install python-pip python-setuptools python-yaml python-distribute python-docutils python-dateutil python-six  


$ sudo pip install rosdep rosinstall_generator wstool rosinstall   
１回目うまくいかなかったので２回目は、pip2にしてみた。
$ sudo <font color="Red">pip2</font> install rosdep rosinstall_generator wstool rosinstall  

rosdepの初期化  
$ sudo rosdep init  
$ rosdep update

<font color="Red">２回目もうまくいかなかったので、３回目は再起動してここからやり直した。</font>　　

catkin Workspaceの作成  
$ mkdir ~/ros_catkin_ws  
$ cd ~/ros_catkin_ws  

ROS packageとcommunication librariesのコンパイル(w/o rqt, rviz, and robot-generic libraries)    
$ rosinstall_generator ros_comm --rosdistro indigo --deps --wet-only --exclude roslisp --tar > indigo-ros_comm-wet.rosinstall
(5分ぐらい反応ないけど待っていると終わる)  
$ wstool init src indigo-ros_comm-wet.rosinstall  

catkin workspace依存ライブラリのビルドとインストール  
ROS packageとcommunication librariesだけをRaspbian Jessieにインストールする場合は特に何もする必要なし。  

依存関係の解決  
$ cd ~/ros_catkin_ws
$ rosdep install --from-paths src --ignore-src --rosdistro indigo -y -r --os=debian:jessie

catkin Workspaceのコンパイル　　
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/indigo -j2 　


環境設定ファイルをロードするように設定しておく  
$ echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
$ source ~/.bashrc

### 動作テスト 1  
ROSのマスターを起動  
$roscore  
無事、roscoreが起動できました。

### ワークスペースをGitHubリポジトリ内のフォルダに作成
リポジトリ内のワークスペースを作成したいフォルダへ移動後srcフォルダを作成
$mkdir src
$cd src
試しにビルドしてみる
$cd ..
$catkin_make

ROSの環境設定を設定しなおしリロードする  
(~/.bashrcに追加したコードを以下のように編集)
```bash
# Set ROS Indigo
source /opt/ros/indigo/setup.bash
source ~/github/Study_for_Autonomous_Sumobot_Jr/ROS_Raspi/devel/setup.bash

# Set ROS Network
export ROS_HOSTNAME=ホスト名
export ROS_MASTER_URI=http://${ROS_HOSTNAME}:11311

# Set ROS alias command
alias cw='cd ~/github/Study_for_Autonomous_Sumobot_Jr/ROS_Raspi/'
alias cs='cd ~/github/Study_for_Autonomous_Sumobot_Jr/ROS_Raspi/src'
alias cm='cd ~/github/Study_for_Autonomous_Sumobot_Jr/ROS_Raspi/ && catkin_make'
```
$ source ~/.bashrc

### 動作テスト 2
##### Ubuntu14.04LTS+ROS IndigoをインストールしたPCで
$roscore      
$rosrun turtlesim turtlesim_node     
$rosrun turtlesim turtle_teleop_key

##### Raspberry_piで
$rostopic list
※rostopic listはうまくいくので通信はうまく行っているようです。

$rostopic echo /turtle1/cmd_vel  
とすると『ERROR: Cannot load message class for [geometry_msgs/Twist]. Are your messages built?』というエラーメッセージが出ます。  

##### トライ①
$cs  
$https://github.com/ros/std_msgs  
$cm  
$source ~/.bashrc  
$rostopic echo /turtle1/cmd_vel  
まだ、『ERROR: Cannot load message class for [geometry_msgs/Twist]. Are your messages built?』というエラーメッセージが出ます。
