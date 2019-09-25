def isValid(s):
    dict={'(':1,')':2,'{':3,'}':4,'[':5,']':6}
    flag1=0
    flag2=0
    flag3=0
    #for i in range(len(s)):
        #print(dict.get(s[i]))
    for i in range(len(s)):
        if flag1==0:
            if dict.get(s[i])==2:
                return False
                #print("Hi,1")
        elif flag2==0:
            if dict.get(s[i])==4:
                return False
                #print("Hi,2")
        elif flag3==0:
            if dict.get(s[i])==6:
                return False
                #print("Hi,3")
        elif dict.get(s[i])==1:
            flag1=1
            #print("Hi,4")
        elif dict.get(s[i])==3:
            flag2=1
            #print("Hi,5")
        elif dict.get(s[i])==5:
            flag3=1
            #print("Hi,6")
        elif flag1==1:
            if dict.get(s[i])==2:
                flag1=0
                #print("Hi,7")
        elif flag2==1:
            if dict.get(s[i])==4:
                flag2=0
                #print("Hi,8")
        elif flag3==1:
            if dict.get(s[i])==6:
                flag3=0
                #print("Hi,9")
    if flag1==1 or flag2==1 or flag3==1:
        #print("Hi,10")
        return False
    else:
        return True
        #print("Hi,11")
