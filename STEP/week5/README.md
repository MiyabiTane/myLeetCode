## STEP Week5

### 宿題<br>
巡回セールスマン問題を解こう。できるだけ最短距離になるようなプログラムを作る。<br>

コードなど、詳細は[google-step-tspリポジトリ](https://github.com/MiyabiTane/google-step-tsp/tree/step2020)<br>

＜方法１＞<br>
貪欲法 + 交差を取り除く。<br>
N = 2048だけ最後の一本がうまくいかなかった。<br>
行き順の結果はmy_ans/remove_crossに出力した。<br>

＜方法２＞
kmeansでグループ分けしてその中で方法１で解いて、最後に近い順で繋げる。<br>
距離が伸びてしまいました。。。<br>

距離の結果は
```
Challenge 0
my_ans/remove_cross/output:    3418.10
my_ans/kmeans/output:    3418.10
sample/random   :    3862.20
sample/greedy   :    3418.10
sample/sa       :    3291.62

Challenge 1
my_ans/remove_cross/output:    3832.29
my_ans/kmeans/output:    3942.55
sample/random   :    6101.57
sample/greedy   :    3832.29
sample/sa       :    3778.72

Challenge 2
my_ans/remove_cross/output:    4974.50
my_ans/kmeans/output:    5130.60
sample/random   :   13479.25
sample/greedy   :    5449.44
sample/sa       :    4494.42

Challenge 3
my_ans/remove_cross/output:   10155.75
my_ans/kmeans/output:   11492.22
sample/random   :   47521.08
sample/greedy   :   10519.16
sample/sa       :    8150.91

Challenge 4
my_ans/remove_cross/output:   12128.92
my_ans/kmeans/output:   15199.06
sample/random   :   92719.14
sample/greedy   :   12684.06
sample/sa       :   10675.29

Challenge 5
my_ans/remove_cross/output:   23499.91
my_ans/kmeans/output:   28421.24
sample/random   :  347392.97
sample/greedy   :   25331.84
sample/sa       :   21119.55

Challenge 6
my_ans/remove_cross/output:   46737.15
my_ans/kmeans/output:   58057.38
sample/random   : 1374393.14
sample/greedy   :   49892.05
sample/sa       :   44393.89
```