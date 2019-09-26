#def merge(nums1,m,nums2,n):
#    nums1=nums1[:m]+nums2[:n]
#    nums1.sort()
#    return nums1

def merge(nums1,m,nums2,n):
    nums1[m:m+n]=nums2[:n]
    nums1=nums1[:m+n]
    nums1.sort()
    return nums1
