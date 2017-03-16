# Ubuntu 14.04 LTS + Python + Juliusで音声認識
[Raspberry Piで音声認識](http://qiita.com/t_oginogin/items/f0ba9d2eb622c05558f4)や[\[Raspberry Pi\]USBマイクと音声認識ソフトJuliusを使って音声認識を試す\(3\)　~ フルカラーLEDを音声で操作 ~](http://blog.livedoor.jp/sce_info3-craft/archives/9248622.html)を参考にして作業を進めました。

#### 必要なソフトをインストール
$ sudo apt-get update  
$ sudo apt-get upgrade  
$ sudo apt-get install alsa-utils sox libsox-fmt-all
$ sudo apt-get install pavucontrol  

#### マイク（プラグインと内臓）のCard No と Device Noを調べる
$ arecord -l  
※私の環境ではヘッドセットはカード2, デバイス0でした

#### alsamixerでマイク音量（プラグインと内臓）を設定する
※なぜかUSBヘッドセットをささないとalsamixerが起動できませんでした。
$ alsamixer
F6(サウンドカード選択)→HDA Intel PCH
Auto-Muto : Disable
その他をすべて１００にしてESCで終了

#### alsamixerでマイク音量（プラグインor内臓）を１００に設定する
$ pavucontrol  
入力タブの音量設定を１００にする

#### 録音してみる
$ arecord -D plughw:2,0 -r 16000 -f S16_LE test.wav  
※2,0 はカード番号の2とデバイス番号の0  
※16000はJulius用に16kHz  
※終了はctl+c  

#### 再生してみる
$ aplay test.wav

### Juliusの環境設定  
#### ダウンロードとコンパイルとインストール
$cd ~
$wget --trust-server-names   'http://osdn.jp/frs/redir.php?m=iij&f=%2Fjulius%2F60273%2Fjulius-4.3.1.tar.gz'  
$ tar xvzf julius-4.3.1.tar.gz  
$ cd julius-4.3.1/  
$ ./configure  
$ make
$ rm julius-4.3.1.tar.gz   

##### ディクテーションファイルの取得取得  
$ mkdir ~/julius-4.3.1/  
$ cd ~/julius-4.3.1/   
$ wget --trust-server-names   'http://osdn.jp/frs/redir.php?m=iij&f=%2Fjulius%2F60416%2Fdictation-kit-v4.3.1-linux.tgz'  
$ tar xvzf dictation-kit-v4.3.1-linux.tgz  
$ rm dictation-kit-v4.3.1-linux.tgz

##### エイリアス（別名）とシンボリックリンク
このままでは実行時のコマンドがものすごく長くなってしまうので、エイリアス（別名）とシンボリックリンクを設定します  
$ nano ~/.bashrc  
　　最終行に以下を追加
```
# Juliusのalias
alias julius='~/julius-4.3.1/julius/julius'
```
$source ~/.bashrc
$ln -s ~/julius-4.3.1/dictation-kit-v4.3.1-linux/ julius_dic

##### Juliusの実行(waveファイル)
$ julius -C ~/julius_dic/am-gmm.jconf -C ~/julius_dic/main.jconf -input rawfile  
※16kHzで録音されてる必要あり。


##### Juliusの実行(マイクから)
$ ALSADEV="plughw:2,0" julius -C ~/julius_dic/am-gmm.jconf -C ~/julius_dic/main.jconf -nostrip

##### オリジナルディクテーションファイルの作成
command.yomi
```
右 みぎ
左 ひだり
前進  ぜんしん
後退  こうたい
止まれ とまれ
```
※言葉+タブ+ひらがな＋改行
※最終行には改行を入れない

$iconv -f utf8 -t eucjp command.yomi | ~/julius_dic/bin/yomi2voca.pl > ~/julius_dic/command.dic

##### オリジナルディクテーション設定ファイルの作成
$ nano ~/julius_dic/command.jconf
```
-w command.dic
-v model/lang_m/bccwj.60k.htkdic
-h model/phone_m/jnas-tri-3k16-gid.binhmm
-hlist model/phone_m/logicalTri
-lmp 8.0 -2.0
-lmp2 8.0 -2.0
-b 1500
-b2 100
-s 500
-m 10000
-n 30
-output 1
-input mic
-zmeanframe
-rejectshort 800
-charconv EUC-JP UTF-8
```
##### オリジナルディクテーションファイルの動作確認
###### マイクから
$ ALSADEV="plughw:2,0" julius -C ~/julius_dic/command.jconf -nostrip  

###### WAVファイルから  
$ julius -C ~/julius_dic/command.jconf -input rawfile

# USBヘッドセット関連の設定(うまくいかなかったので参考)
※使用したヘッドセット：Logicool製ですが、型番は不明です。
※いろいろ試したけどUbuntu 14.04LTS + USBヘッドセット　+ Julius rev.4.3.1の組み合わせでは、1度は起動できるけど、2度目の起動前はUSBを抜き差ししないといけないという不具合ではまり、解決できませんでした。[こちらの方](http://engetu21.hatenablog.com/entry/2014/11/16/155927)も同じ現象が起きているので、そういうものだと思って諦めました。

#### USB機器として認識されているか確認する  
$lsusb  
私の環境では問題なく認識されていました。

#### USBヘッドセットの優先順位の確認
$cat /proc/asound/modules  
 0 snd_hda_intel  
 1 snd_hda_intel  
 2 snd_usb_audio  

#### USBヘッドセットの優先順位の変更
$sudo nano /etc/modprobe.d/alsa-base.conf  

\# Keep snd-usb-audio from beeing loaded as first soundcard     
options snd-usb-audio index=-2  

の行を以下に書き換える

\# Keep snd-usb-audio from beeing loaded as first soundcard  
options snd-usb-audio index=0

#### 再起動してUSBヘッドセットの優先順位の確認
$sudo reboot  
$cat /proc/asound/modules  
0 snd_usb_audio  
1 snd_hda_intel  
2 snd_hda_intel

#### USBヘッドセットのCard No と Device Noを調べる
$ arecord -l
※私の環境ではヘッドセットはカード2, デバイス0でした

##### Juliusの実行(USBヘッドセットから)
$ ALSADEV="plughw:0,0" julius -C ~/julius_dic/am-gmm.jconf -C ~/julius_dic/main.jconf -nostrip

うまく起動できない時は、USBを抜いて    
$ fuser /dev/snd/*  
USBをさして  
$ fuser /dev/snd/*  
pcmc***が消えるまで上記コマンドを実行してから、再実行するとうまく起動できる

#### USBヘッドセットのトラブルシュートで使ったコマンド
※Ubuntuの別の音関連の不具合対策にもつかえると思う

$ cat /proc/asound/cards
$ cat /proc/asound/modules  
$ arecord -l
$ sudo apt-get install pavucontrol
$ pavucontrol
$ alsamixer
