def checkValidString(s):
    keep = []
    for i,sig in enumerate(s):
        if sig == ')':
            if keep and (keep[-1] == '('):
                keep.pop()
            elif len(keep)>=2 and (keep[-2:] == ['(','*']):
                if i!=len(s)-1 and s[i+1]==')':
                    continue
                keep = keep[:-2]
            elif len(keep)>=3 and (keep[-3:] == ['(','*',')']):
                keep = keep[:-3]
            elif keep and (keep[-1] == '*'):
                keep.pop()
            else:
                return False
        elif sig == '(':
            keep.append(sig)
        elif sig == '*':
            if keep[-1] == '(':
                keep.append(sig)
        print(keep)
    if (')' in keep) or ('(' in keep):
        return False
    return True


ans = checkValidString("(*()")
print(ans)
        
            
