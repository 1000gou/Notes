# 電気工作関連のメモ

## 電気のおさらい
### オームの法則  
V = IR
V:電圧[V]、Ｉ電流[A]、Ｒ抵抗[Ω]

### キルヒホッフの法則
電流と電圧の結合則　　  

###### 直列　　
R = R1+R2  
V = V1+V2  
I = I1 = I2  

###### 並列
V = V1 = V2  
I = I1+I2  
1/R = 1/R1 + 1/R2    

### 電気回路の記号とよく使う値
抵抗：単位　Ω（オーム）  
コンデンサー：Ｆ（ファラッド）  
インダクタ：Ｈ（ヘンリー）  

ダイオード：  
バイポーラトランジスタ：  
  ＰＮＰトランジスタ、ＮＰＮトランジスタ  
ＭＯＳトランジスタ：  
　Ｎ型、Ｐ型  

### LTspice(電気回路のシミュレータ)
インストール方法：[LTspice入門：Windows版の入手とインストール](http://easylabo.com/2014/10/ltspice/2313/)   
(参考)[初心者のためのLTspice入門の入門](http://www.denshi.club/ltspice/2015/03/ltspice1.html)

### LTspice使いかた
#### 新規回路の作成  
File -> New Schematic  

#### コンポーネントの配置
電源：コンポーネント（F2）-> VOLTAGE    
ダイオードの配置：コンポーネント（F2）-> DIODE    
抵抗の配置：コンポーネント（F2）-> res  
GNDの配置：EDIT -> Place GND  
配線：  

※値（ＶやΩなど）の入力は、コンポーネントの上にカーソルを持っていくとアイコンが指差しマークになるので、その時右クリック。  

#### シミュレーション：  
右クリック → Draft → Spice directivesで以下のコマンドを入力する

###### .Tran : 過渡（周波数成分あり）  
例：```.tran 0 10m```  
0～10ms

###### .DC : 直流の解析
例：```.DC V1 0 2.0 0.01```    
V1:電源の名前、0 2.0 0.01: 0～2Vまで0.01刻み   

###### .AC : 横軸＝周波数、縦軸＝ゲイン  


###### シミュレーションの開始→RUN  
電圧をグラフに電圧に出したいときは配線をクリック、電流を出したいときはコンポーネントをクリック。







　
