def isValid(s):
    left1=0;left2=0;left3=0
    for i in range(len(s)):
        if s[i]=='(':
            left1+=1
        elif s[i]=='{':
            left2+=1
        elif s[i]=='[':
            left3+=1
        elif s[i]==')':
            left1-=1
            if left1<0:
                return False
        elif s[i]=='}':
            left2-=1
            if left2<0:
                return False
        elif s[i]==']':
            left3-=1
            if left3<0:
                return False
    if left1==0 and left2==0 and left3==0:
        return True
    else:
        return False
