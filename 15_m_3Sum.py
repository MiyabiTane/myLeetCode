def threeSum(nums):
    ans=[]
    if len(nums)<3:
        return []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            sum=nums[i]+nums[j]
            if -1*sum in nums[j+1:]:
                ans.append([nums[i],nums[j],-sum])
    #print(ans)
    l=len(ans[0])-1
    while l>0:
        #print(l)
        #print([ans[l][0],ans[l][1],ans[l][2]])
        if ([ans[l][0],ans[l][1],ans[l][2]] in ans[:l]) or ([ans[l][0],ans[l][2],ans[l][1]] in ans[:l]) or ([ans[l][1],ans[l][0],ans[l][2]] in ans[:l]) or ([ans[l][1],ans[l][2],ans[l][0]] in ans[:l]) or ([ans[l][2],ans[l][0],ans[l][1]] in ans[:l]) or ([ans[l][2],ans[l][1],ans[l][0]] in ans[:l]):
            ans.pop(l)
            l-=1
        l-=1
    return ans
