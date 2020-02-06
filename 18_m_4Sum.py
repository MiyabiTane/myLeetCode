def fourSum(nums,target):
    nums.sort()
    #print(nums)
    answer=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            p1=j+1;p2=len(nums)-1
            while p1<p2:
                want_sum=target-(nums[i]+nums[j])
                #print("{},{} : p1={},p2={},want_sum={}".format(nums[i],nums[j],p1,p2,want_sum))
                if nums[p1]+nums[p2]<=want_sum:
                    if nums[p1]+nums[p2]==want_sum:
                        if not [nums[i],nums[j],nums[p1],nums[p2]] in answer:
                            answer.append([nums[i],nums[j],nums[p1],nums[p2]])
                    p1+=1
                else:
                    p2-=1
    return answer

nums=[-3,-2,-1,0,0,1,2,3]
target=0
answer=fourSum(nums,target)
print(answer)
