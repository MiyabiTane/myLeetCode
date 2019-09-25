def longestCommonPrefix(strs):
    flag=0
    flag2=0
    ans=""
    if strs==[]:
        ans=""
    elif len(strs)==1:
        ans=strs[0]
    else:
        while(flag2==0):
            for i in range(min(len(strs[0]),len(strs[1]))):
                if strs[0][i]==strs[1][i]:
                    for j in range(len(strs)):
                        if strs[j][i]!=strs[0][i]:
                            flag=1
                            flag2=1
                    if flag==0:
                        ans+=strs[0][i]
                else:
                    flag2=1
    return ans
