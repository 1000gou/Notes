## Gazebo (シミュレーター)

### Gazeboのインストール
$sudo apt-get install ros-indigo-kobuki-gazebo   

### Gazeboの実行   
$roslaunch kobuki_gazebo kobuki_playground.launch

1. トラブル：
Error [Node.cc:90] No namespace found  
解決法:
モジュールのダウンロードに時間がかかっているだけなのでしばらく待ってからGazeboを再起動する。

1. トラブル：  
画面が真っ暗で何も表示されない。Rvizでも真っ暗なのと関係がある？  
解決法：  
どうやら、OpenGLのエラーらしい([情報元](http://demura.net/lecture/12406.html)）。
以下のコマンドを./bashrcの最後に追加する。
```$export LIBGL_ALWAYS_SOFTWARE=1```

## Gazebo (シミュレーター)とRviz(データ可視化)
### Turtlebotのシミュレート
[turtlebot_gazeboのシミュレーションデモを動かす](http://qiita.com/wakoruru/items/532879f273f966277379)を参照して行った。

$sudo apt-get install ros-indigo-turtlebot-gazebo  
$source ~/.bashrc  
$roslaunch turtlebot_gazebo turtlebot_world.launch    
$roslaunch turtlebot_gazebo amcl_demo.launch  

```
ここでエラーが出る場合は  
$ roscd turtlebot_gazebo/launch/  
$ sudo nano amcl_demo.launch

<include file="$(find turtlebot_navigation)/launch/includes/amcl.launch.xml">
を
<include file="$(find turtlebot_navigation)/launch/includes/amcl/amcl.launch.xml">
に変更する。```

$rosrun rviz rviz  

rvizでロボットのモデル等を追加する。   
[Add]→[By display type]→[RobotModel]  
[Add]→[By Topic]→[/map]→[Map]  
[Add]→[By Topic]→[/camera]→[/depth]→[/points]→[PointCloud2]  
[Add]→[By Topic]→[/odom]→[Odometry]  
[Add]→[By Topic]→[/move_base]→[/NavfnROS]→[/plan]→[Path]  

rvizでロボットの目的地と方向を指定する。  
[2DNavGoal]を押し目的地をクリックして方向をドラッグする。  
