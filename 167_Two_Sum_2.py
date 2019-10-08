def TwoSum(numbers,target):
    left=0
    right=len(numbers)-1
    while(left<right):
        if numbers[left]+numbers[right]==target:
            return [left+1,right+1]
        elif numbers[left]+numbers[right]<target:
            while(numbers[left]==numbers[left+1]):
                left+=1
            left+=1
        else:
            while(numbers[right]==numbers[right-1]):
                right-=1
            right-=1
        #print("left:right= ",left,":",right)
