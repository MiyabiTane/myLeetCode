def search(nums,target):
    def search_and_count(nums,target,count):
        if len(nums)==0:
            return -1
        if target==nums[0]:
            return count
        else:
            return -2

    count=0
    answer=-2
    while answer==-2:
        answer=search_and_count(nums,target,count)
        count+=1
        nums=nums[1:]
        #print("nums={}, count={}, answer={}".format(nums,count,answer))
    return answer

ans=search([4,5,6,7,0,1,2],target=3)
print(ans)
