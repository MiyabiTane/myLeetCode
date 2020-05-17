from collections import Counter
def findAnagrams(s: str, p: str):
    n = len(s); m = len(p)
    ans = []
    for i in range(n-m+1):
        if sorted(Counter(s[i:i+m]).items()) == sorted(Counter(p).items()):
            ans.append(i)
    return ans


ans = findAnagrams("abab"
                   ,"ab")
print(ans)

