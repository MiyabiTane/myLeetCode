import numpy as np
def spiralOrder(matrix):
    if matrix==[]:
        return []
    #どこをすでに通ったかの記録
    seen=np.zeros((len(matrix),len(matrix[0])), dtype=np.int)
    seen=np.pad(seen, (1,1), 'constant', constant_values=(1,1))
    #matrixをseenと同じ形に
    dummy=np.pad(matrix, (1,1), 'constant')
    #print(seen)
    #print(dummy)

    ip=1; jp=1
    ans=[]
    while True:
        ans.append(dummy[ip][jp])
        seen[ip][jp]=1
        if seen[ip][jp-1]==1 and seen[ip-1][jp]==1 and seen[ip][jp+1]==1 and seen[ip+1][jp]==1: 
            break
        elif seen[ip][jp-1]==1 and seen[ip-1][jp]==1 and seen[ip][jp+1]==0:
            jp+=1
        elif seen[ip-1][jp]==1 and seen[ip][jp+1]==1 and seen[ip+1][jp]==0:
            ip+=1
        elif seen[ip][jp+1]==1 and seen[ip+1][jp]==1 and seen[ip][jp-1]==0:
            jp-=1
        elif seen[ip][jp-1]==1 and seen[ip+1][jp]==1 and seen[ip-1][jp]==0:
            ip-=1
    return ans

ans=spiralOrder([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(ans)