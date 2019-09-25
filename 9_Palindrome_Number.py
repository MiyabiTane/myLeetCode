def isPalindrome(x):
    list=[]
    flag=0
    if x<0:
        flag=1
    elif x>0:
        while(x!=0):
            list.append(int(x%10))
            x=(x-(x%10))/10
            #print(list)
        for i in range(len(list)/2+1):
            if len(list)%2==0:
                if list[i]!=list[len(list)-i-1]:
                    flag=1
            elif len(list)%2!=0:
                if i!=len(list)/2:
                    if list[i]!=list[len(list)-i-1]:
                        flag=1
    if flag==0:
        return True
    else:
        return False
