def generateParenthesis(n):
    answer=[]
    if n==0:
        return [""]
    elif n==1:
        return ["()"]
    else:
        pre_answer=generateParenthesis(n-1)
        for i in range(len(pre_answer)):
            answer.append("("+pre_answer[i]+")")
            answer.append("()"+pre_answer[i])
            #if ("()"+pre_answer[i])!=(pre_answer[i]+"()"):
            answer.append(pre_answer[i]+"()")
        answer=[a for a in set(answer)]
    return answer

an=generateParenthesis(4)
print(an)
