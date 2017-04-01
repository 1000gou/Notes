# ESP-WROOM-32

## ESP-WROOM-32メモ(Windows編)
### 開発環境の構築
※基本的に[ESP32(ESP-WROOM-32)でLチカ (WindowsでArduino IDE使用)](http://qiita.com/rukihena/items/6a904368700eb1c7d2a3)を参考にしながら作業を行いましたが、理解できないところがあったので、経験者に教わりました。

1. [公式ページ](http://qiita.com/rukihena/items/6a904368700eb1c7d2a3)よりArduino IDEをダウンロードしインストールする。（2017/4/1時点で最新版のarduino-1.8.2-windows.exeをダウンロードしてインストールしました。）

1. https://github.com/espressif/arduino-esp32.git にアクセス→Clone or download　→　Download ZIP

1. C:\Users\ユーザー名\Documents\Arduino\
の中に\hardware\espressiff\esp32というフォルダを作り、その中にダウンロードしたZIPの中身(cores, docなど)をすべてコピー。

1. Aruduinoを起動し、以下のコードをコピペし、適当な名前で保存する。

```c
#include <dummy.h>
#define PORT 26

void setup() {
  pinMode(PORT, OUTPUT);
}

void loop() {
  digitalWrite(PORT, HIGH);
  delay(1000);
  digitalWrite(PORT, LOW);
  delay(1000);
}
```

1. ツール→ボードから"ESP 32Dev Module"を選択。
1. ツール→ボードからシリアルポートを選択（私の環境ではCOM3）でした。
※その他はそのまま、Flash Frequency"80MHz"、Upload Speed"921600"
1. 配線は"GPIO26ピン→抵抗→LED→GND"を直列につなぐ。
1. スケッチ　→　マイコンボードに書き込む (Ctl+U)

以上で無事書き込むことが出来ました。
配線と動作の様子は[ESP32でLチカできました](https://twitter.com/1000gou/status/848067879102631936)にツイートしておきました。
