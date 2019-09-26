def lengthOfLastWord(s):
    ans=""
    flag=0
    for i in range(len(s)-1,-1,-1):
        if s[i]==' ' and flag==1:
            break
        elif s[i]!=' ':
            flag=1
            ans+=s[i]
        #print(ans)
    return len(ans)
