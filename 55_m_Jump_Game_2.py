#ボトムアップDP
def canJump(nums):
    #そこから初めて最後のマスにたどり着ける -> Good
    #たどり着けない -> Bad
    memo =["N"]*len(nums) #Good or False
    memo[-1]="G"
    for i in range(len(nums)-2,-1,-1):
        furthestJump=min(i+nums[i], len(nums)-1)
        for j in range(i+1,furthestJump+1):
            if memo[j]=="G":
                memo[i]="G"
                break
    if memo[0]=="G":
        return True
    return False    

ans=canJump([2,3,1,1,4])
print(ans)

