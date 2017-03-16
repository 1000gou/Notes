## ROSコマンド
### ROSコマンド (パッケージの実行)  
<font color="Green">roscoreの実行</font>  
$roscore  

turtlesimパッケージのturtlesim_nodeの実行    
$rosrun turtlesim turtlesim_node  

turtlesimパッケージのturtle_teleop_key実行    
$rosrun turtlesim turtle_teleop_key

### ROSコマンド (パッケージ情報の取得)
ヘルプの表示  
$rospack -h　

パッケージリストの表示  
$rospack list

依存するパッケージのリストを表示  
$rospack depends パッケージ名

依存するパッケージをインデント形式で表示  
$rospack depends-indent turtlesim

パッケージの中で定義されているメッセージを表示  
$rosmsg package パッケージ名     

### ROSコマンド (ノードを調べる)
rosnodeのヘルプ  
$rosnode -h  

アクティブなノードを表示  
$rosnode list -a  

ノードの情報を表示  
$rosnode info ノード名  

<font color="Green">ノードの停止</font>  
$rosnode kill  

ノードが停止されたのに登録情報が残っている場合  
$rosnode cleanup  

ノードにPingする  
$rosnode ping ノード名

### ノード間の通信
#### トピック：publisherとsubscriberの間で非同期通信（subscriberは複数でも良い）
<font color="Green">トピックの可視化ツール</font>  
$rosrun rqt_graph rqt_graph
($rqt_graphでも同じ)

<font color="Green">ROSのコンソールの表示</font>  
$rqt_console  

トピックのヘルプ  
$rostopic -h  

現在流れているトピックのリスト  
$rostopic list  

<font color="Green">トピックの現在値を表示</font>   
$rostopic echo トピック名

<font color="Green">トピックを発行</font>  
$rostopic pub トピック名  
（例）rostopic pub -r 1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0,0.0,0.0]' '[0.0,0.0,1.8]'

#### サービス ：サービスサーバとサービスクライアントの双方向通信
サービスコマンドに関するヘルプ  
$rosservice -h  

現在ノードが提供しているサービスのリストを表示  
$rosservice list

サービスが受け取るメッセージの型を調べる  
$rosservice type サービス名 | rossrv show  
(例)$rosservice type /kill | rossrv show  

サービスを呼び出す  
$rosservice call サービス名　パラメータ

### パラメータ
（ノードが持っているで変数で外部から参照や操作できるものこと？）  

パラメータの一覧を表示  
$rosparam list

パラメータを取得  
$rosparam get パラメータ名  

パラメータをセット   
$rosparam set パラメータ名 値  

### Launchファイル（複数のノードの実行）
※以下のようなlauchファイル(*.launch)を作成  
```
<launch>
  <node pkg="ros_start" name = "talker" type = "talker.py"/>
  <node pkg="ros_start" name = "listener" type = "listener.py"/>
</launch>
```    
※パッケージの中にlaunchというフォルダを作成し、その中にlaunchファイルを作成した場合は  
$roslaunch パッケージ名　launchファイル名   

そうでないときは
$roslaunch launchファイルの相対パス  

<font color="Red">※マスターが立ち上がっていないときは、自動的にマスターが起動される。</font>
