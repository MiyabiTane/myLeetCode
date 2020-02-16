def combinationSum(candidates, target):
    candidates.sort()
    answer=[]
    #バックトラック法：手を進め切ったら一つ戻ってやり直す。
    def BackTracking(candidates, target, temp):
        for can in candidates:
            if can>target:
                return #一つ前に戻る
            temp.append(can)
            if can==target:
                copy=temp.copy() #copyを使わないとanswerの中身もpopされてしまう。
                answer.append(copy)
                temp.pop()
            else:   #can<targetならもう一度その数字から調べる。
                index=candidates.index(can)
                BackTracking(candidates[index:], target-can, temp)
                temp.pop()

    BackTracking(candidates, target, [])
    return answer

answer=combinationSum([2,3,6,7],7)
print(answer)
