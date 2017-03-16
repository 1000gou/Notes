## ROSでJoystick

### UbuntuへのJoystick（speed link sl-650000-BK）のインストール
$ sudo apt-get install joystick jstest-gtk  
システムツール → jstest-gtkで、ボタンごとの信号が見れる。

### joy_node(Joystickドライバ)のインストール
$sudo apt-get update  
$sudo apt-get install ros-indigo-joy

### joy_nodeの信号のTopicを見る
$roscore  
$rosrun joy joy_node  
$rostopic echo joy  

### joy_node から twist topicを生成するパッケージを使う
$ sudo apt-get install ros-indigo-teleop-twist-joy

$rosrun joy joy_node
$rosrun teleop_twist_joy teleop_node
