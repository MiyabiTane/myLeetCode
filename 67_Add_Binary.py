def addBinary(a,b):
    if (not a):
        return b
    elif (not b):
        return a
    else:
        if a[-1]=='0' and b[-1]=='0':
            return addBinary(a[:-1],b[:-1])+'0'
        elif a[-1]=='1' and b[-1]=='1':
            return addBinary(addBinary(a[:-1],b[:-1]),'1')+'0'
        else:
            return addBinary(a[:-1],b[:-1])+'1'
            
