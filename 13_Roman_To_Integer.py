def RomanToInt(s):
    dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans=0
    flag=0
#if dict.get(key)<dict.get(key), it is special
    for i in range(len(s)):
        if i!=len(s)-1 and dict.get(s[i])<dict.get(s[i+1]):
            #print("%d-%d"%(dict.get(s[i+1]),dict.get(s[i])))
            ans+=dict.get(s[i+1])-dict.get(s[i])
            flag=1
        elif flag==1:
            flag=0
        else:
            ans+=dict.get(s[i])
        #print(ans)
    return ans
