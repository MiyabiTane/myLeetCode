def search(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if target==nums[mid]:
            return mid
        #右半分がソートされている時
        if nums[mid]<nums[right]:
            #targetが右半分にあれば
            if target>nums[mid] and target<=nums[right]:
                left=mid+1
            #targetが左半分にあれば
            else:
                right=mid-1
        #左半分がソートされている時
        else:
            #targetが左半分にあれば
            if target>=nums[left] and target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
    return -1
    
ans=search([4,5,6,7,0,1,2],target=0)
print(ans)
