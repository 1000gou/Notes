# OpenJTalkを使ってみる
[『OpenJTalk + python で日本語テキストを発話』](http://qiita.com/kkoba84/items/b828229c374a249965a9)を参考にして、作業を行いました。

### RaspberryPiを持ってなかったので、OpenJTalkをUbuntuへインストール
$ sudo apt-get install open-jtalk  
$ sudo apt-get install open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001

MMDAgent(女性の声)を取得し解凍
$ wget https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip/download -O MMDAgent_Example-1.6.zip  
$ unzip MMDAgent_Example-1.6.zip MMDAgent_Example-1.6/Voice/*

Voiceデータを移動
$sudo cp -r MMDAgent_Example-1.6/Voice/mei/ /usr/share/hts-voice

### サンプルプログラム(01_Jtalk_Python2.py)
```Python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def speek_by_jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

if __name__ == '__main__':
    speek_by_jtalk("こんにちは")
```
