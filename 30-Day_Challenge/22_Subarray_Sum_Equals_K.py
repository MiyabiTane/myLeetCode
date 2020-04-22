def subarraySum(nums,k):
    sum = 0
    map = {0:1}
    count = 0
    for num in nums:
        sum += num
        if (sum - k) in map:
        # sum - k in map ということは 和がsum - kになった場所の次のインデックスからの和がkということ
            count += map.get(sum-k)
        if sum in map:
            map[sum] += 1
        else:
            map[sum] = 1
        
    #print(map)
    return count

ans = subarraySum([1,2,1,2,1],3)
print(ans)



