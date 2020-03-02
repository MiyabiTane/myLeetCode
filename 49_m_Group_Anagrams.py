
def groupAnagrams(strs):
    dict={}
    for str in strs:
        key=tuple(sorted(str))
        if tuple(sorted(str)) in dict: #listはkeyにできない
            dict[key].append(str)
        else:
            dict[key]=[str]
    #print(dict)
    ans=list(dict.values())
    #print(ans)
    return ans
    
"""
import collections
def groupAnagrams(strs):
    #存在しないkeyを参照しても大丈夫
    ans=collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())
"""

strs=["are","bat","ear","code","tab","era"]
ans=groupAnagrams(strs)
print(ans)