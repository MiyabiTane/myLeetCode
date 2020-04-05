def moveZeros(nums):
    pos=0
    for i in range(len(nums)):
        if nums[pos]==0:
            nums = nums[:pos]+nums[pos+1:]+[nums[pos]]
        else:
            pos+=1
    return nums

ans = moveZeros([0, 1, 0, 3, 12])
print(ans)


