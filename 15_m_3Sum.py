def threeSum(nums):
    nums.sort()
    ans=[]
    if len(nums)<3:
        return ans
    for i in range(len(nums)):
        if i!=0 and nums[i]==nums[i-1]:
            #print("continue")
            continue
        target=-nums[i]
        j=i+1;k=len(nums)-1
        while j<k:
            if nums[j]+nums[k]==target:
                ans.append([nums[i],nums[j],nums[k]])
                j+=1;k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k1]==nums[k]:
                    k-=1
            elif nums[j]+nums[k]<target:
                j+=1
            else:
                k-=1
    return ans
