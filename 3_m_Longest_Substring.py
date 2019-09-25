def lengthOfLongestSubstring(s):
    list1=[]
    count=0
    flag=0
    for i in range(len(s)):
        if s[i] in list1:
            if len(list1)>count:
                count=len(list1)
            list1=list1[list1.index(s[i])+1:]
            flag=1
        list1.append(s[i])
        print(list1)
    if flag==0 or len(list1)>count:
        return len(list1)
    return count
