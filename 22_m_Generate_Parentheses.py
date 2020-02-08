#"("の数と")"の数に注目
def generateParenthesis(n):
    answer=[]
    def backtrack(S="",left=0,right=0):
        if len(S)==2*n:
            answer.append(S)
            #print(answer)
        #elifにしないことで全パターンを調べることができる。
        if left<n:
            backtrack(S+'(',left+1,right)
        if right<left:
            backtrack(S+')',left,right+1)
    backtrack()
    return answer

an=generateParenthesis(3)
print(an)
