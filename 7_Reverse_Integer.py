def reverse(nums):
    list=[]
    i=1
    flag=0
    if nums<0:
        flag=1
        nums=nums*(-1)
    while(nums!=0):
        list.append(nums%10)
        nums=(nums-list[i-1])/10
        i+=1
    list.reverse()
    #print(list)
    b=1
    ans=0
    for i in range(len(list)):
        ans+=list[i]*b
        #print(ans)
        b*=10
    if flag==1:
        if (-1)*(2**31)<=ans*(-1):
            return ans*(-1)
        else:
            return 0
    else:
        if ans<=2**31-1:
            return ans
        else:
            return 0
