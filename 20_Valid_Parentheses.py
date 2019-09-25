def isValid(s):
    dict={')':'(','}':'{',']':'['}
    Stack=[]
    for i in range(len(s)):
        if Stack==[]:
            Stack.append(s[i])
        else:
            mark=Stack[-1]
            if dict.get(s[i])==mark:
                Stack.pop()
            else:
                Stack.append(s[i])
        #print(Stack)
    if Stack==[]:
        return True
    else:
        return False
