def judge(board):
    def Dangojudge(array):
        count=0
        for st in array:
            if st=='o':
                count+=1
                if count==3:
                    return 1
            else:
                count=0
        return 0

    #checkpoint1
    for i in range(5):
        row=[board[i][j] for j in range(5)]
        check1=Dangojudge(row)
        if check1==1:
            return "Dango"
    #checkpoint2
    for i in range(5):
        col=[board[j][i] for j in range(5)]
        check2=Dangojudge(col)
        if check2==1:
            return "Dango"
    #checkpoint3
    for diff in range(-2,3):
        diag=[]
        for i in range(5):
            for j in range(5):
                if i-j==diff:
                    diag.append(board[i][j])
        check3=Dangojudge(diag)
        if check3==1:
            return "Dango"
    for sum in range(2,7):
        diag=[]
        for i in range(5):
            for j in range(5):
                if i+j==sum:
                    diag.append(board[i][j])
        check3=Dangojudge(diag)
        if check3==1:
            return "Dango"
    return "Dango deha nai yo!"

ans=judge([['x','o','x','o','o'],
 ['o','o','x','o','x'],
 ['o','x','x','x','o'],
 ['x','o','x','o','o'],
 ['o','o','x','o','x']])
print(ans)

