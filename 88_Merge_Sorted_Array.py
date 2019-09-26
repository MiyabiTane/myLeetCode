def merge(nums1,m,nums2,n):
    nums3=nums1
    nums3=nums3[:m]
    nums2=nums2[:n]
    i=0

    print(nums3)
    print(nums2)

    while nums2 and nums3:
        if nums2[0]<=nums3[0]:
            nums1[i]=nums2[0]
            nums2=nums2[1:]
            i+=1
        else:
            nums1[i]=nums3[0]
            nums3=nums3[1:]
            i+=1
        #print("here,0")
    #if not nums2 or not nums3:
        #nums1[i+1:i+1+len(nums3)]=nums3 or nums1[i+1:i+1+len(nums2)]=nums2
    if not nums2:
        nums1[i:i+len(nums3)]=nums3
        #print("here,1")
    elif not nums3:
        nums1[i:i+len(nums2)]=nums2
        #print("here,2")
    return nums1
