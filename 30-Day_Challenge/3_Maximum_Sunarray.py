def maxSubArray(nums):
    max_num = nums[0]
    max_pre = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > max_pre+nums[i]:
            max_pre= nums[i]
        else:
            max_pre += nums[i]
        if max_pre > max_num:
            max_num = max_pre
    return max_num


ans = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(ans)
