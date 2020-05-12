def singleNonDuplicate(nums):
    left = 0; right = len(nums)-1
    while left < right:
        middle = (left + right) // 2
        if middle % 2 == 1:
            middle -= 1
        if nums[middle] != nums[middle+1]:
            right = middle
        else:
            left = middle + 2
    return nums[left]

ans = singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
print(ans)




