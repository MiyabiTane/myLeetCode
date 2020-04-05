def singleNumber(nums):
    dict={}
    for num in nums:
        if num in dict:
            dict[num]+=1
        else:
            dict[num]=0
    ans = [k for k, v in dict.items() if v == 0][0]
    return ans

ans =singleNumber([2,2,1])
print(ans)
    
            
