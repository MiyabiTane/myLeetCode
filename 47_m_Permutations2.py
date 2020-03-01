def permuteUnique(nums):
    nums.sort()
    ans=[]
    def like_backtrack(nums,seen,tmp,d):
        if d==len(nums):
            copy=tmp.copy()
            ans.append(copy)
            return
        for i in range(len(nums)):
            if seen[i]==0:
                #同じ数字は飛ばす
                if i>0 and nums[i]==nums[i-1] and seen[i-1]==0:
                    continue    
                tmp[d]=nums[i]
                seen[i]=1
                like_backtrack(nums,seen,tmp,d+1)
                seen[i]=0
                tmp[d]=0    

    seen=[0]*len(nums) 
    tmp=[0]*len(nums)
    like_backtrack(nums,seen,tmp,0)
    return ans

ans=permuteUnique([1,1,2])
print(ans)

#参考:https://www.youtube.com/watch?v=snAviXjcfpY
