def permuteUnique(nums):
    #count : [1,1,2,4]->[0,2,1,0,1,0...]
    #d : 一つの順列を作り終えたか判断
    ans=[]
    def like_backtrack(nums,count,tmp,d):
        if d==len(nums):
            copy=tmp.copy()
            if not copy in ans:
                ans.append(copy)
            return
        else:
            for i in range(len(nums)):
                if count[nums[i]]==0:
                    continue
                count[nums[i]]-=1
                tmp[d]=nums[i]
                like_backtrack(nums,count,tmp,d+1)
                count[nums[i]]+=1
                tmp[d]=0

    count=[0]*10 
    for i in range(len(nums)):
        count[nums[i]]+=1
    tmp=[0]*len(nums)
    like_backtrack(nums,count,tmp,0)
    return ans

ans=permuteUnique([1,1,2])
print(ans)


