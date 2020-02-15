import numpy as np
def isValidSudoku(board):
    #数字があればそれを格納
    row_list=[[] for i in range(len(board))]
    col_list=[[] for i in range(len(board[0]))]
    box_list=[[] for i in range(9)]
    r_count=0
    c_count=0
    b_count=0
    plus=3
    for i in range(len(board)):
        r_count+=1
        c_count=0
        for j in range(len(board[0])):
            c_count+=1
            if j%3==0:
                b_count+=1
                if b_count==4:
                    b_count=1
            if ((i+1)*(j+1))%27==0:
                b_count+=plus
            print("b_count={}".format(b_count))
            #print("row={},column={},box={}".format(r_count,c_count,b_count))
            #格納
            if board[i][j]!=".":
                keep_num=int(board[i][j])
                row_list[r_count-1].append(keep_num)
                col_list[c_count-1].append(keep_num)
                box_list[b_count-1].append(keep_num)
    print(np.array(row_list))
    print(np.array(col_list))
    print(np.array(box_list))
    if ([] in row_list) or ([] in col_list) or ([] in box_list):
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
