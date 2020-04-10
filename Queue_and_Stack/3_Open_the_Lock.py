from collections import deque
def openLock(deadends, target):
    qu = deque([("0000",0)])
    visited = ["0000"]
    while qu:
        num, count = qu.popleft()
        if num == target:
            return count
        elif num in deadends:
            continue
        for i in range(4):
            #数字を一つ上げる
            new_num = num[:i]+str((int(num[i])+1)%10)+num[i+1:]
            if not new_num in visited:
                visited.append(new_num)
                qu.extend([(new_num,count+1)])
            #数字を一つ下げる
            new_num = num[:i]+str((int(num[i])+9)%10)+num[i+1:]
            if not new_num in visited:
                visited.append(new_num)
                qu.extend([(new_num, count+1)])
    return -1




ans = openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
print(ans)
        


 
    
    

