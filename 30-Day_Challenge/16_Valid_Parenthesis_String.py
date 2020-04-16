def checkValidString(s):
    #'('と')'の数だけに注目すれば良い。*はあり得るパターンをメモすればいい。
    low = 0; high =0
    for sig in s:
        if sig == '(':
           low += 1; high += 1
        elif sig == ')':
            low -= 1; high -= 1
        elif sig == '*':
            low -= 1 #もし*が)だったら
            high += 1 #もし*が(だったら
        low = max(0, low) #low<0の時点でFalse
        if high < 0: #)が一番左にきてしまった時
            return False
        #print(low, high)
    #lowとhighの間に0がある、すなわち左右の()数が等しくなり得る時
    if low == 0:
        return True
    return False


ans = checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
print(ans)
        
            
