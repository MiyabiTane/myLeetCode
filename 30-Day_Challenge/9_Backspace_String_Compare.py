def backspaceCompare(S, T):
    def makeStr(S):
        back_count = 0
        ans=""
        for s in S[::-1]:
            if s == "#":
                back_count+=1
            elif back_count>0:
                back_count-=1
            else:
                ans+=s
        return ans
    S = makeStr(S)
    T = makeStr(T)
    print("S,T= ",S," ",T)
    if S==T:
        return True
    return False


ans = backspaceCompare("ab#c","ad#c")
print(ans)


