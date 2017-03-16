## Hello World with ROS + Python
※『ROSではじめるロボットプログラミング』(ISBN978-4-7775-1901-9)の７章を参考にしておこないました。

##### パッケージの作成
$cs  
$catkin_create_pkg ros_start rospy std_msgs  

##### Makeする
$cm  

##### Makeしたパッケージ(ros_start)をシェルに登録  
$source ~/.bashrc

##### 作成したパッケージのフォルダへ移動  
$ros_cd ros_start

##### Pythonプログラムを保存するフォルダを作成
※Pythonプログラムはパッケージ内にscriptsというフォルダを作成しそこに保存する。  
$mkdir scripts  
$cd scripts  

##### talker.pyとlistener.pyをscriptsに保存
###### talker.py
```Python
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('chatter', String, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    hello_str = String()
    hello_str.data ="Hello world %s" % rospy.get_time()
    pub.publish(hello_str)
    rate.sleep()
```  

###### listener.py
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-# -*- coding: UTF-8 -*-

import rospy
from std_msgs.msg import String

def callback(message):
    rospy.loginfo("I heard %s", message.data)

rospy.init_node('listener')
sub = rospy.Subscriber('chatter', String, callback)

#無限ループで待つ
rospy.spin()
```

##### talker.pyとlistener.pyをscriptsを登録
talker.pyとlistener.pyに実行権限を与える（必要？)    
$chmod 755 talker.py listener.py

makeする（必要？）  
$cm  

シェルへ登録(必要？)  
$source ~/.bashrc

##### 作成したプログラムの動作テスト
$roscore  
$rosrun ros_start talker.py  
$rosrun ros_start listener.py  
