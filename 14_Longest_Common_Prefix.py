def longestCommonPrefix(strs):
    if strs==[]:
        return ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i>=len(string):
                return strs[0][:i]
            elif string[i]!=strs[0][i]:
                return strs[0][:i]
    return strs[0]
