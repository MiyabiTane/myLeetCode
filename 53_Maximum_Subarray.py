def sum(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum

def hantei(nums):
    for i in nums:
        if i>0:
            return 0
    return 1

def maxSubArray(nums):
    l=[]
    max=nums[0]
    for i in range(len(nums)):
        sum_before=sum(l)
        #l.append(nums[i])
        #if sum(l)<0:
        #    l=[]
        if nums[i]<0:
            max=sum(l)
        l.append(nums[i])



        print(l,sum(l))
    return sum(l)
    if hantei(nums)==1:
        return max(nums)
