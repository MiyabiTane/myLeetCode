def nextPermutation(nums):
    list=[]
    for i in range(len(nums)):
        pointer=len(nums)-1-i
        #print(pointer)
        if pointer==0:
            nums.sort()
            return nums
        list.append(nums[pointer])
        if nums[pointer-1]<nums[pointer]:
            list.append(nums[pointer-1])
            list.sort()
            #print(list)
            for j in range(len(list)):
                if list[j]>nums[pointer-1]:
                    rem_num=list.pop(j)
                    break
            nums[pointer-1]=rem_num
            nums[pointer:]=list
            return nums

nums=nextPermutation([1,3,2])
print(nums)
