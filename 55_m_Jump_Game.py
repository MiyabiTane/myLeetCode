#トップダウンDP : 一度計算したものは記憶しておいて２回目は計算しないようにする。
def canJump(nums):
    #そこから初めて最後のマスにたどり着ける -> Good
    #たどり着けない -> Bad
    memo =["N"]*len(nums) #Good or False
    def canJumpFromPosition(pos, nums):
        if memo[pos]=="G": 
            return True
        furtherstJump=min(pos+nums[pos], len(nums)-1)
        for i in range(pos+1, furtherstJump+1):
            if canJumpFromPosition(i, nums):
                memo[pos]="G"
                return True
        memo[pos]="B"
        return False

    memo[-1]="G"
    return canJumpFromPosition(0, nums)


ans=canJump([3,2,1,0,4])
print(ans)

