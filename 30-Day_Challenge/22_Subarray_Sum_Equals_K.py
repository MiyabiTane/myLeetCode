def subarraySum(nums,k):
    count = 0
    sum = [0]
    for i in range(1,len(nums)+1):
        sum.append(sum[i-1]+nums[i-1])
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)+1):
            if sum[j] - sum[i] == k:
                count+=1
    return count

ans = subarraySum([1,1,1],2)
print(ans)



