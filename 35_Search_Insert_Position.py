def searchInsert(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    if target>nums[-1]:
        return len(nums)
    return 0
