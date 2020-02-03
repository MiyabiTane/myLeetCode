def threeSumClosest(nums,target):
    nums.sort()
    min_diff=100000
    for i in range(len(nums)):
        p1=i+1;p2=len(nums)-1
        print("p1:{}, p2:{}".format(p1,p2))
        want_to_get=target-nums[i]
        while p1<p2:
            diff=(nums[p1]+nums[p2])-want_to_get
            if diff==0:
                return target
            else:
                if abs(diff)<abs(min_diff):
                    ans=diff+target
                    min_diff=diff
                if diff<0:
                    p1+=1
                else:
                    p2-=1
            print(min_diff)
    return target+min_diff
