def longestPalindrome(s):
    list=[0,0]
    max=0
    count=0
    ans=[]
    for i in range(len(s)):
        """if list==[0,0]:
            if count>max:
                max=count
            count=0"""
        if s[i]==list[-1]:
            list.pop(i+1)
            count+=2
            if count>max:
                max=count
        elif s[i]==list[-2]:
            list.pop(i+1)
            list.pop(i)
            count+=3
            if count>max:
                max=count
        else:
            list.append(s[i])

    return max
