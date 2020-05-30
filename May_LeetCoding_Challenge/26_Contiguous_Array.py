def findMaxLength(nums):
    #memo key:sum value:index
    memo = {0:1}
    sum = 0
    max_len = 0
    for i,num in enumerate(nums):
        if num == 0:
            sum -= 1
        elif num == 1:
            sum += 1

        if sum in memo:
            #同じ値になるということはその間にある０と１の数が等しいということ
            leng = i - memo[sum]
            if leng > max_len:
                max_len = leng
        else:
            memo[sum] = i
    return max_len


ans = findMaxLength([0, 1, 0])
print(ans)
