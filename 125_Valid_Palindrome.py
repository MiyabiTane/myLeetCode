def isPalindrome(s):
    if s=="":
        return True
    for i in range(len(s)):
        if s[i].isalnum()==False:
            s=s[:i]+','+s[i+1:]
    s=s.replace(',','')
    s=s.lower()
    print(s)
    for i in range(len(s)):
        if s[i]!=s[-(i+1)]:
            return False
    return True
