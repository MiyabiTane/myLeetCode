def search(nums , target):
    left = 0; right = len(nums)-1
    while left <= right:
        print(left,right)
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        #右側がソートされてる時
        if nums[mid] < nums[right]:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        #左側がソートされている時
        elif nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


ans = search([1,3,5], 1)
print(ans)
        





