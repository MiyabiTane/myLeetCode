def isPalindrome(s):
    if s=="":
        return True
    s=s.replace(':','')
    s=s.replace(',','')
    s=s.replace(' ','')
    s=s.replace('.','')
    s=s.lower()
    print(s)
    for i in range(len(s)):
        if s[i]!=s[-(i+1)]:
            return False
    return True
