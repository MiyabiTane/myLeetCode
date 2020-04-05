def moveZeros(nums):
    p1=0; p2=0
    while p2!=len(nums):
        while nums[p2]==0:
            p2+=1
            if p2==len(nums):
                return nums
        if p1!=p2:
            nums[p1],nums[p2] = nums[p2],nums[p1]
        p1+=1; p2+=1
    return nums

ans = moveZeros([0])
print(ans)


