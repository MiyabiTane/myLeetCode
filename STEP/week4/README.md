## STEP Week4

### 宿題１<br>
Dummy SNSのフォロー・フォロワー関係を使って、"adrian"から自分（"johnnie"）にたどり着けるか調査してみよう<br>

幅優先探索を使った方法<br>
```
python3 ./homework1_BFS.py --links [(ID)\t(ID)形式のテキストファイル] --nicknames [(ID)\t(名前)形式のテキストファイル] --start [出発点の人の名前] --target [到達できるか調べたい相手の名前]
```
例：adrianからjohnnieまでたどり着けるか調べる。
```
./homework1.py --links links.txt --nicknames nicknames.txt --start "adrian" --target "johnnie"
```