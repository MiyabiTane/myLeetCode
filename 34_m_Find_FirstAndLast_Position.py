def searchRange(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        print("mid={}".format(mid))
        if target==nums[mid]:
            ans_if=mid
            rig=mid
            lef=mid
            while True:
                if rig==len(nums)-1:
                    break
                elif nums[rig+1]!=target:
                    print("right={}".format(rig))
                    break
                rig+=1
            while True:
                if lef==0:
                    break
                elif nums[lef-1]!=target:
                    print("left={}".format(lef))
                    break
                lef-=1
            return [lef,rig]
        elif nums[left]<=target and target<=nums[mid]:
            right=mid-1
        else:
            left=mid+1
    return [-1,-1]

ans=searchRange([3,4,5,6,6,7,8],6)
print(ans)
