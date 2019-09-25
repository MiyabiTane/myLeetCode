def longestPalindrome(s):
    max_count=0
    if s=="":
        return ""
    start=0
    end=0
    check=[[0 for i in range(len(s))] for j in range(len(s))] #init
    for i in range(len(s)):
        check[i][i]=1
        for j in range(0,i):
            #print(j,i)
            if s[j]==s[i] and (check[j+1][i-1]==1 or i-j<=2):
                check[j][i]=1
                #print("Hello")
                if i-j>max_count:
                    max_start=j
                    max_end=i
                    max_count=i-j
    #print(check)
    return s[max_start:max_end+1]
