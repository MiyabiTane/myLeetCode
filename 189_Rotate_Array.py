def rotate(nums,k):
    #reverse left, reverse right ->reverse whole
    #don't need to remine the number -> O(1)
    if len(nums)<2:
        return nums
    k=k%len(nums)

    def partreverse(nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1

    partreverse(nums,0,len(nums)-k-1)
    partreverse(nums,len(nums)-k,len(nums)-1)
    partreverse(nums,0,len(nums)-1)

    return nums
