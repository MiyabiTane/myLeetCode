def countAndSay(n):
    if n==1:
        return "1"
    num="1"
    for i in range(n-1):
        say=""
        count=0
        s_before=num[0]
        for s in num:
            if s==s_before:
                count+=1
            else:
                say+=str(count)+s_before
                count=1
                s_before=s
        say+=str(count)+s_before
        num=say
        #print(say)
    return say
