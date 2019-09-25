def removeDuplicates(nums):
    leng=0
    if nums==[]:
        return 0
    else:
        for i in range(len(nums)):
            if nums[leng]!=nums[i]:
                leng+=1
                nums[leng]=nums[i]
        return leng+1
