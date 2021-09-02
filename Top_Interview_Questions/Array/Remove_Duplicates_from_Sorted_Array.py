def removeDuplicates(nums):
    N = len(nums)
    count = 0
    i = 1
    while i < N:
        if nums[i] != 101 and nums[i] == nums[i - 1]:
            count += 1
            nums = nums[:i] + nums[i + 1:] + [101]
            # print(nums, count)
        else:
            i += 1
    # print(nums, count)
    return N - count

nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)