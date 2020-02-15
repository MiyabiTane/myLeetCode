import numpy as np
def isValidSudoku(board):
    #check row
    for i in range(9):
        row=[]
        for j in range(9):
            if board[i][j]!=".":
                row.append(int(board[i][j]))
        #print(row)
        if len(set(row))!=len(row):
            return False
    #check column
    for i in range(len(board[0])):
        col=[board[j][i] for j in range(9) if board[j][i]!="."]
        #print(col)
        if len(set(col))!=len(col):
            return False
    #check sub-boxes
    for i in range(0,9,3):
        for j in range(0,9,3):
            sub_box=[]
            for x in range(3):
                for y in range(3):
                    if board[i+x][j+y]!=".":
                        sub_box.append(board[i+x][j+y])
            #print(sub_box)
            if len(set(sub_box))!=len(sub_box):
                return False
    return True

ans=isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
print(ans)
