def findMaxLength(nums):
    memo = [0]*(len(nums)+1)
    max_len = 0
    #0がきたら-1,1がきたら+1
    for i,num in enumerate(nums):
        i+=1
        if num == 0:
            memo[i] = memo[i-1]-1
        if num == 1:
            memo[i] = memo[i-1]+1
        if memo[i] in memo:
            if (i - memo.index(memo[i])) > max_len: #重複したら一番最初のindexを返す
                max_len = i - memo.index(memo[i])
        print(memo)
    return max_len


ans = findMaxLength([0,1])
print(ans)
