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
        check=[]
        for j in range(i+1,len(nums)):
            if j>1 and nums[j]==nums[j-2]:
                continue
            target_2=target-nums[j]
            if (target_2 in nums[j+1:])and (not (target_2 in check)):
                ans.append([nums[i],nums[j],target_2])
                check.append(nums[j]
    return ans
