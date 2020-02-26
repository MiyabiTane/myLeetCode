def permute(nums):
    def sub_permute(inte,nums):
        if len(nums)==2:
            inte2=inte.cppy()
            inte.append(nums[0])
            inte.append(nums[1])
            inte2.append(nums[1])
            inte2.append(nums[0])
            return [inte,inte2]
        else:
            list=[]
            for i in range(len(nums)):
                copy=nums.copy()
                copy.pop(i)
                list.append(sub_permute(nums[i],copy))
            return list
    
    if len(nums)==0:
        return []
    elif len(nums)==1:
        return [nums]
    elif len(nums)==2:
        return [[nums[0],nums[1]],[nums[1],nums[0]]]
    else:


ans=permute([1,2,3])
print(ans)


    