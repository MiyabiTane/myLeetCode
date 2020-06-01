## STEP Week3

### 宿題１<br>
モジュール化を意識して電卓のプログラムに"\*"と"/"の機能を追加しよう<br>

＜方法１＞<br>
"\*"と"/"を評価した後、"+"と"-"を評価する二段階評価法。evaluateの中に全て書くと見にくいと思ったので、firstEvaluate, secondEvaluateという２つのfunctionを作りました。また、"\*"と"/"を読むreadMalti, readDevisというfunctionも作りました。<br>

```
python3 ./homework1.py
```

＜方法２＞<br>
"2\*2"や"3/4\*2"など、*や/で繋がった文字列を「数字」としてreadNumberの中で読み込んでしまおうと考えました。readNumber中のコードが多くなってしまいますが、あくまでreadNumber関数を呼ぶだけで良いようにした方がうまくモジュール化できている気がしたので、readNumberの中をさらにモジュール化することで分かりやすくしました。<br>
```
python3 ./homework1_eval_one_time.py 
```

### 宿題２<br>
できるだけ網羅的になるようにテストケースを追加しよう。<br>


### 宿題３<br>
括弧に対応しよう。<br>

stackを使って()が閉じるごとに中身が評価されるようにしました。functionが増えて分かりにくくなってしまったのでfunctionにコメントでinput, outputなどの説明を加えるようにしました。また、Week1にユーザーの入力を信じすぎてはいけないというお話があったのでユーザーの入力が悪い時はなるべくInvalid Syntaxと表示してプログラムを落とすようにして、エラーにならないようにしました。<br>

＜方法１＞に加えたもの<br>
```
python3 ./homework3.py
```

＜方法２＞加えたもの<br>
```
python3 ./homework3_eval_one_time.py 
```


