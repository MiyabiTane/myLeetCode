def myAtoi(str):
    list=['0','1','2','3','4','5','6','7','8','9','-','+']
    ans=[]
    flag=0
    flag2=0
    flag3=0
    #print(4 in list)
    #print(str[0] in list)
    if str=="":
        return 0
    for i in range(len(str)):
        if (str[i] in list)==False and str[i]!=' ':
            break
            if flag!=1 and flag2!=1:
                return 0
        elif (flag2==1 or flag==1 or flag3==1) and str[i]==' ':
            break
        elif str[i] in list:
            if flag2==1 and (str[i]=='+' or str[i]=='-'):
                break
            elif str[i]=='-':
                flag=1
            elif str[i]=='+':
                flag3=1
            else:
                ans.append(str[i])
                flag2=1
    #print(ans)
    inte=0
    for i in range(len(ans)):
        inte+=int(ans.pop(-1))*10**i
    if flag==1:
        inte=-1*inte
    #print(inte)
    if inte<(-2)**31:
        return (-2)**31
    elif inte>2**31-1:
        return 2**31-1
    elif flag==1 and flag3==1:
        return 0
    else:
        return inte
    """ans_map=map(str,ans)
    if flag==1:
        result=''-'+'.join(ans_map)
    else:
        result=''.join(ans_map)
    return result"""
