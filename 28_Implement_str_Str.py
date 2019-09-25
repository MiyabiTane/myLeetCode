def strStr(haystack,needle):
    flag=0
    j=0
    if haystack=="" or needle=="":
        if needle!="":
            return -1
        else:
            return 0
    elif len(needle)>len(haystack):
        return -1
    else:
        for i in range(len(haystack)):
            if haystack[i]==needle[j]:
                mark=i
                flag=1
                break
        #print(mark)
        if flag==1:
            if len(haystack)-mark<len(needle):
                return -1
            else:
                for i in range(mark,mark+len(needle)):
                    #print(haystack[i])
                    if haystack[i]!=needle[i-mark]:
                        flag=0
    if flag==1:
        return mark
    else:
        return -1
