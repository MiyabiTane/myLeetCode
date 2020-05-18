from collections import Counter
def checkInclusion(s1: str, s2: str):
    leng = len(s1)
    ans = []
    s1Counter = Counter(s1)
    s2Counter = Counter(s2[:leng-1])
    for i in range(leng-1, len(s2)):
        head = i-leng+1
        #s[i]がもともと入っていなくても可
        s2Counter[s2[i]] += 1  # windowにchar追加
        if s2Counter == s1Counter:
            return True
        s2Counter[s2[head]] -= 1  # remove head from window
        if s2Counter[s2[head]] == 0:
            del s2Counter[s2[head]]
    return False


ans = checkInclusion("ab", "eidboaoo")
print(ans)
