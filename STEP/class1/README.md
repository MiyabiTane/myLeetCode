## STEP Week1


### 宿題１<br>

anagramを見つける<br>
https://gist.github.com/MiyabiTane/1a5984421ebdd4dc3a31243846081f9b


### 宿題２<br>
ゲームで高得点を目指す<br>
https://gist.github.com/MiyabiTane/ecba18fafb3e27ad12a658724342cac4


## Mentor's FeedBack

Gist参照のこと<br>


### 全体的なアドバイス<br>

・空の入力""がバグになることが多いのでテストケースとして必ず確認すること。<br>
・anagramで自分自身を返さないようにする部分について、辞書自体を変えてしまうのは実用的でなく、よくない。<br>
・"qu"に関するルールについて。辞書の単語を信用しすぎてはいけない。辞書中にルールを満たさない単語があれば省いてしまって良い。<br>


### オマケ<br>

・２問目<br>
TreeNode使うともっと早く探索できる
```
class TreeNode(object):
    def __init__(self):
        self.hash = ''
        self.val = 0
        self.children = defaultdict(TreeNode)
```



