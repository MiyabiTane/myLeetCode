def canJump(nums):
    #i:後ろからのステップ数
    for i in range(len(nums)):
        num=nums[len(nums)-1-i]
        if num==i and i==len(nums)-1:
            return True
        elif num==i:
            return canJump(nums[:-i])
        elif i==len(nums)-1:
            return False

ans=canJump([2,3,1,1,4])
print(ans)

