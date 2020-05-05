def firstUniqChar(s: str) -> int:
    for i in range(len(s)):
        if not s[i] in s[:i]+s[i+1:]:
            return i
    return -1


ans = firstUniqChar("cc")
print(ans)
    

