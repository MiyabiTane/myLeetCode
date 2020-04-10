from collections import deque
def openLock(deadends, target):
    qu = deque([(0,0,0,0)])
    count = [0]*4
    while qu:
        i,j,k,l = qu.popleft()
        if str(i)+str(j)+str(k)+str(l)==target:
            return min(count)
        if not str(i)+str(j)+str(k)+str((l+1)%10) in deadends:
            qu.extend([(i,j,k,(l+1)%10)])
            count[0]+=1
        if not str(i)+str(j)+str((k+1)%10)+str(l) in deadends:
            qu.extend([(i,j,(k+1)%10,l)])
            count[1]+=1
        if not str(i)+str((j+1)%10)+str(k)+str(l) in deadends:
            qu.extend([(i,(j+1)%10,k,l)])
            count[2]+=1
        if not str((i+1)%10)+str(j)+str(k)+str(l) in deadends:
            qu.extend([((i+1)%10,j,k,l)])
            count[3]+=1
        print(count)
        if len(qu)==0:
            return -1


ans = openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
print(ans)
        


 
    
    

