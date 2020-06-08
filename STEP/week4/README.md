## STEP Week4

### 宿題１<br>
Dummy SNSのフォロー・フォロワー関係を使って、"adrian"から自分（"johnnie"）にたどり着けるか調査してみよう<br>

幅優先探索を使った方法<br>
```
python3 ./homework1_BFS.py --links [(ID)\t(ID)形式のテキストファイル] --nicknames [(ID)\t(名前)形式のテキストファイル] --start [出発点の人の名前] --target [到達できるか調べたい相手の名前]
```

深さ優先探索を使った方法<br>
```
python3 ./homework1_DFS.py --links [(ID)\t(ID)形式のテキストファイル] --nicknames [(ID)\t(名前)形式のテキストファイル] --start [出発点の人の名前] --target [到達できるか調べたい相手の名前]
```

adrianからjohnnieにたどり着けるか調べるのにいくつの辺を通ったかをカウントしてみた（たどり着けた場合のみ数値を返す）<br>

幅優先探索
```
./homework1_BFS.py --links links.txt --nicknames nicknames.txt --start "adrian" --target "johnnie"
```
```
3
True
```

深さ優先探索
```
python3 ./homework1_DFS.py --links links.txt --nicknames nicknames.txt --start "adrian" --target "johnnie"
```
```
37
True
```
たどり着けた！<br>
深さ優先探索では幅優先探索に比べてだいぶ遠回りしてしまっていることがわかった。<br>