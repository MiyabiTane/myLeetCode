def strStr(haystack,needle):
    if haystack=="" or needle=="":
        if needle!="":
            return -1
        else:
            return 0
    elif len(needle)>len(haystack):
        return -1
    else:
        for i in range(len(haystack)):
            #if haystack[i]==needle[0]:
                #if needle in haystack[i:]:
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
