def majorityElement(nums):
    dict={}
    set_num=list(set(nums))
    for num in set_num:
        dict[num]=0
    for num in nums:
        dict[num]+=1
    #print(dict)
    #pop the key satisfied the value conditions
    ans=[k for k,v in dict.items() if v>=(len(nums)//2+len(nums)%2)][0]
    return ans
