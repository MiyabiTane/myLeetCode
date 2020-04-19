def search(nums , target):
    if 0 < len(nums) <= 2:
        if len(nums) == 0:
            return -1
        if nums[0] == target:
            return 0
        if len(nums) == 2:
            if nums[1] == target:
                return 1
    left = 0; right = len(nums)-1
    while (left + 1) < right:
        print(left,right)
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        #右側がソートされてる時
        if nums[mid] <= nums[right]:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid
        #左側がソートされている時
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        else:
            left += 1
    return -1


ans = search([1,3,5], 1)
print(ans)
        





