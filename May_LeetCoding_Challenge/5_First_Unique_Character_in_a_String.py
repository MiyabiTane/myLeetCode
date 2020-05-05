import collections
def firstUniqChar(s: str) -> int:
    #key:要素　value:出現回数 の辞書が作られる 
    hashMap = collections.Counter(s)
    
    for i,st in enumerate(s):
        if hashMap[st] == 1:
            return i
    return -1 

ans = firstUniqChar("loveleetcode")
print(ans)
    

