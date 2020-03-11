#Greedy
def canJump(nums):
    #そこから初めて最後のマスにたどり着ける -> Good
    #たどり着けない -> Bad
    left=len(nums)-1 #一番左にあるGood
    for i in range(len(nums)-1,-1,-1):
        #leftより右のマスにたどり着けるなら必ずleftに行くことができる。すなわちiはGoodPos
        if i+nums[i] >= left: 
            left=i
    if left==0:
        return True
    return False
            

ans=canJump([3,2,1,0,4])
print(ans)

