def combinationSum2(candidates, target):
    candidates.sort()
    answer=[]
    def BackTracking(candidates, target, temp):
        for can in candidates:
            if can>target:
                return 
            temp.append(can)
            if can==target:
                copy=temp.copy()
                if not copy in answer:
                    answer.append(copy)
                temp.pop()
            else:
                index=candidates.index(can)
                if index!=len(candidates)-1:
                    BackTracking(candidates[min(len(candidates)-1,index+1):],target-can,temp)
                temp.pop()

        
    BackTracking(candidates, target, [])
    return answer

ans=combinationSum2([1],2)
print(ans)


