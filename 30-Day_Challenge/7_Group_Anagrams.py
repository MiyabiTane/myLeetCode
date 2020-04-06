def groupAnagrams(strs):
    dict_list=[]
    ans=[]
    for str in strs:
        dict={}
        for s in str:
            if s in dict:
                dict[s]+=1
            else:
                dict[s]=1
        if dict in dict_list:
            ans[dict_list.index(dict)].append(str)
        else:
            ans.append([str])
            dict_list.append(dict)
    return ans


ans = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(ans)
