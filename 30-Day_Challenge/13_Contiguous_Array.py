def findMaxLength(nums):
    memo = {0:-1}
    max_len = 0
    sum = 0
    #0がきたら-1,1がきたら+1
    for i,num in enumerate(nums):
        if num == 0:
            sum -= 1
        if num == 1:
            sum += 1
        if sum in memo:
            max_len = max(max_len, i-memo[sum])
        else:
            memo[sum] = i
    return max_len


ans = findMaxLength([0,1,0])
print(ans)
