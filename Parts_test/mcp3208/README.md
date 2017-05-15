# ADコンバータ：MCP3208の動作テスト

### 情報
[Raspberry PiのPythonからTMP36のアナログ温度センサとMCP3008のADコンバータを使う](http://qiita.com/masato/items/f089a17b1c9329eb7d03)  
[WebIOPiでIoT！(6)プログラミング応用編~アナログ入力編](http://deviceplus.jp/hobby/raspberrypi_entry_035/)

### SPIが有効になっているか確認する  
 $ lsmod | grep spi


### py-spidevのインストール
$ git clone git://github.com/doceme/py-spidev
$ cd py-spidev
$ sudo python2 setup.py install  
もしくは、
$ sudo python3 setup.py install

### サンプルプログラム
[サンプルプログラム:mcp3208.py](mcp3208.py)
