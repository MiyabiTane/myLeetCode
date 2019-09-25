def removeDuplicates(nums):
    if nums==[]:
        return 0
    mark=nums[0]
    try:
        for i in range(len(nums)):
            if nums[i]==mark and nums[i]!=nums[-1]:
                nums.pop(i)
            mark=nums[i+1]
            print("%d:%d"%(mark,nums))
    except:
        pass
    print(nums)
    return len(nums)

    #mark=nums[0]
    ##because of nums.pop(),out of range occurs
    #for i in range(len(nums)):
    #    if nums[i]==mark:
    #        nums.pop(i)
    #        if i!=len(nums)-1:
    #            mark=nums[i]
    #        print(mark)
    #return len(nums)
