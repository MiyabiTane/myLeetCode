def canJump(nums):
    #その位置から最後のマスにたどり着けるのがGoodマス
    Good_left = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= Good_left:
            Good_left = i
    if Good_left == 0:
        return True
    return False    


ans = canJump([3, 2, 1, 0, 4])
print(ans)
