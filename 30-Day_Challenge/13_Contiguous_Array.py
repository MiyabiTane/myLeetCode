def findMaxLength(nums):
    if len(nums)==0:
        return 0
    
    num_zero = nums.count(0)
    num_one = nums.count(1)
    if num_zero == num_one:
        return len(nums)
    return max(findMaxLength(nums[1:]), findMaxLength(nums[:-1]))

ans = findMaxLength([1,4,1,1,5,3])
print(ans)
