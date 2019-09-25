def convert(s,numRows):
    nums=[[] for i in range(numRows)]
    i=0
    flag=0
    if numRows==1:
        return s
    else:
        for word in s:
            nums[i].append(word)
            if flag==1 and i!=0:
                i-=1
            elif flag==1 and i==0:
                i+=1
                flag=0
            elif i==numRows-1:
                i-=1
                flag=1
            else:
                i+=1
        #print(nums)
    str=""
    while nums:
        if nums[0]==[]:
            nums.pop(0)
            continue
        str+=nums[0].pop(0)
    return str
