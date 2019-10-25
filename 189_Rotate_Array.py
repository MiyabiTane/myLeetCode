def rotate(nums,k):
    if len(nums)<2:
        return nums
    nums_v=[]
    k=k%len(nums)
    for i in range(len(nums)):
        nums_v.append(nums[i])
    #nums_v=nums <-nums_v changes every time when i change
    #print(nums_v)
    #print('')
    for i in range(len(nums_v)):
        nums[i]=nums_v[i-k]
        #print("nums = {}, nums_v = {}".format(nums,nums_v))
        #print("nums_v[{}] is {} ".format(i-k,nums_v[i-k]))
    return nums
    #nums=nums[-k:]+nums[:-k] <= not in-place
