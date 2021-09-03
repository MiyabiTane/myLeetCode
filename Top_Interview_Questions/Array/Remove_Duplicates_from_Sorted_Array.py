def removeDuplicates(nums):
    p1 = 0
    for p2 in range(len(nums)):
        if nums[p1] != nums[p2]:
            p1 += 1
            nums[p1] = nums[p2]
            # print(nums)
    return p1 + 1

# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)
