def productExceptSelf(nums):
    left_product = [1]*len(nums)
    right_product = [1]*len(nums)
    for i in range(1,len(nums)):
        pro = left_product[i-1]*nums[i-1]
        left_product[i] = pro
    #print(left_product)
    for i in range(len(nums)-2,-1,-1):
        pro = right_product[i+1]*nums[i+1]
        right_product[i] = pro
    #print(right_product)
    for i in range(len(nums)):
        left_product[i] *= right_product[i]
    return left_product

ans = productExceptSelf([1, 2, 3, 4])
print(ans)


