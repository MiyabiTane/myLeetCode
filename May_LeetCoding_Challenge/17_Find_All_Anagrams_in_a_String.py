from collections import Counter
def findAnagrams(s: str, p: str):
    leng = len(p)
    ans = []
    pCounter = Counter(p)
    sCounter = Counter(s[:leng-1])
    for i in range(leng-1, len(s)):
        head = i-leng+1
        #s[i]がもともと入っていなくても可
        sCounter[s[i]] += 1 #windowにchar追加
        if sCounter == pCounter:
            ans.append(head)
        sCounter[s[head]] -= 1 #remove head from window
        if sCounter[s[head]] == 0:
            del sCounter[s[head]]
    return ans
        
        
ans = findAnagrams("cbaebabacd", "abc")
print(ans)

