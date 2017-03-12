# Ubuntu 14.04 LTS + Python + Juliusで音声認識
※[Raspberry Piで音声認識](http://qiita.com/t_oginogin/items/f0ba9d2eb622c05558f4)を参考にして作業を進めました。


### USBヘッドセットのインストール
$ヘッドセット：Logicool 型番不明  
###### USB機器として認識されているか確認する  
$lsusb -t

##### USBヘッドセットの選択  
Ubuntu メニュー（画面右上）→システム→サウンドから入出力ともにUSBヘッドセットを選択する


### Juliusの環境設定  
###### ダウンロードとコンパイルとインストール
$wget --trust-server-names   'http://osdn.jp/frs/redir.php?m=iij&f=%2Fjulius%2F60273%2Fjulius-4.3.1.tar.gz'  
$tar xvzf julius-4.3.1.tar.gz  
$cd julius-4.3.1/  
$./configure  
$make  

###### ディクテーションファイルの取得取得  
$ mkdir ~/julius-kits  
$ cd ~/julius-kits  
$ wget --trust-server-names   'http://osdn.jp/frs/redir.php?m=iij&f=%2Fjulius%2F60416%2Fdictation-kit-v4.3.1-linux.tgz'  
$ tar xvzf dictation-kit-v4.3.1-linux.tgz  

###### Juliusの実行
ALSADEV="plughw:0,0" ~/julius-4.3.1/julius/julius -C ~/julius-kits/dictation-kit-v4.3.1-linux/main.jconf -C ~/julius-kits/dictation-kit-v4.3.1-linux/am-gmm.jconf -nostrip
