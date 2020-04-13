def findTargetSumWays(nums, S):
    memo = {}
    n = len(nums)
    def DFS(nums, pos, s): 
        if pos == n:
            if s == S:
                memo[(pos,s)] = 1 #和がSになる組み合わせだった
            else:
                memo[(pos,s)] = 0 #和がSになる組み合わせじゃなかった
        if not (pos,s) in memo:
            memo[(pos,s)] = DFS(nums, pos+1, s-nums[pos])+DFS(nums, pos+1, s+nums[pos])
        #print(memo)
        #print("")
        return memo[(pos,s)]
    DFS(nums, 0, 0)
    return memo[(0,0)]


ans = findTargetSumWays([1, 1, 1, 1, 1], 3)
print(ans)



