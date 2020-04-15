def productExceptSelf(nums):
    def make_products(nums, index):
        pro = 1
        for i,num in enumerate(nums):
            if i != index:
                pro *= num
        return pro
    out = []
    for i in range(len(nums)):
        out.append(make_products(nums, i))
    return out


ans = productExceptSelf([1, 2, 3, 4])
print(ans)


