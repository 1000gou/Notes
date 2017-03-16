## ROSのインストールと環境設定
※ROSのインストールと環境設定は『詳細ROSロボットプログラミング』を参照して行った。

### chronyをインストールして時刻を正確に設定する
$sudo apt-get install chrony  
$sudo ntpdate -q ntp.ubuntu.com

### ROSのインストール
ROSリポジトリアドレスを追加  
$ sudo sh -c ’echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc)main" > /etc/apt/sources.list.d/ros-latest.list’

公開鍵を追加する  
$sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key 0xB01FA116  

インストール  
$ sudo apt-get update  
$sudo apt-get upgrade  
$ sudo apt-get install ros-indigo-desktop-full  
$ sudo apt-get install ros-indigo-rqt*  

rosdepの初期化  
$ sudo rosdep init  
$ rosdep update  

rosinstallのインストール  
$sudo apt-get install python-rosinstall

環境設定ファイルのロード  
$ source /opt/ros/indigo/setup.bash

作業フォルダの作成と初期化  
$ mkdir -p ~/catkin_ws/src  
$ cd ~/catkin_ws/src  
$ catkin_init_workspace  

試しに作業フォルダ内のプログラムをビルド  
$ cd ~/catkin_ws/  
$ catkin_make  

### ROSの環境設定を設定しロードする  
以下のコードを~/.bashrcの最後の行の下に追加
```bash
# Set ROS Indigo
source /opt/ros/indigo/setup.bash
source ~/catkin_ws/devel/setup.bash

# Set ROS Network
export ROS_HOSTNAME=127.0.0.1  #IPアドレスが固定ではないのでととりあえずループバックアドレスを記入した。
export ROS_MASTER_URI=http://${ROS_HOSTNAME}:11311

# Set ROS alias command
alias cw='cd ~/catkin_ws'
alias cs='cd ~/catkin_ws/src'
alias cm='cd ~/catkin_ws && catkin_make'
```
$ source ~/.bashrc

### 動作テスト
ROSのマスターを起動  
$roscore &  

（別ターミナルで）亀がいるウィンドウを作成  
$rosrun turtlesim turtlesim_node   

(別ターミナルで)亀を操作するコントローラーを起動  
$rosrun turtlesim turtle_teleop_key  

カーソルで亀が動くことを確認する

### ワークスペースをGitHubリポジトリ内のフォルダに作成
リポジトリ内のワークスペースを作成したいフォルダへ移動後srcフォルダを作成
$mkdir src
$cd src
$catkin_init_workspace
$cd ..
$catkin_make

ROSの環境設定を設定しなおしリロードする  
(~/.bashrcに追加したコードを以下のように編集)
```bash
# Set ROS Indigo
source /opt/ros/indigo/setup.bash
source ~/GitHubリポジトリ内のフォルダ/devel/setup.bash

# Set ROS Network
export ROS_HOSTNAME=127.0.0.1  #IPアドレスが固定ではないのでととりあえずループバックアドレスを記入した。
export ROS_MASTER_URI=http://${ROS_HOSTNAME}:11311

# Set ROS alias command
alias cw='cd ~/GitHubリポジトリ内のフォルダ'
alias cs='cd ~/GitHubリポジトリ内のフォルダ/src'
alias cm='cd ~/GitHubリポジトリ内のフォルダ && catkin_make'
```
$ source ~/.bashrc
