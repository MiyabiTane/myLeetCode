def myAtoi(str):
    list=['0','1','2','3','4','5','6','7','8','9']
    ans=[]
    isminus=0
    flag=0

    if str=="":
        return 0
    str=str.strip() #remove whitespace character
    for i in range(len(str)):
        if (str[i] in list)==False and flag==1:
            break
        elif (str[i] in list)==False:
            if str[i]=='+' and isminus==0:
                isminus=1
            elif str[i]=='-' and isminus==0:
                isminus=2
            else:
                break
        else:
            ans.append(str[i])
            flag=1
    inte=0
    for i in range(len(ans)):
        inte+=int(ans.pop(-1))*10**i
    if isminus==2:
        inte*=(-1)
    if inte<(-2)**31:
        return (-2)**31
    elif inte>2**31-1:
        return 2**31-1
    else:
        return inte
