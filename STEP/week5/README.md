## STEP Week5

### 宿題<br>
巡回セールスマン問題を解こう。できるだけ最短距離になるようなプログラムを作る。<br>

コードなど、詳細は[google-step-tspリポジトリ](https://github.com/MiyabiTane/google-step-tsp/tree/step2020)<br>

＜方法１＞<br>
貪欲法 + 交差を取り除く。<br>
N = 2048だけ最後の一本がうまくいかなかった。<br>
行き順の結果はmy_ans/remove_crossに出力した。距離の結果は
```
Challenge 0
my_ans/remove_cross/output:    3418.10
sample/greedy   :    3418.10

Challenge 1
my_ans/remove_cross/output:    3832.29
sample/greedy   :    3832.29

Challenge 2
my_ans/remove_cross/output:    4974.50
sample/greedy   :    5449.44

Challenge 3
my_ans/remove_cross/output:   10155.75
sample/greedy   :   10519.16

Challenge 4
my_ans/remove_cross/output:   12128.92
sample/greedy   :   12684.06

Challenge 5
my_ans/remove_cross/output:   23499.91
sample/greedy   :   25331.84

Challenge 6
my_ans/remove_cross/output:   46737.15
sample/greedy   :   49892.05
```