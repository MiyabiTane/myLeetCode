def letterCombinations(digits):
    dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    if ("1" in digits) or (len(digits)==0):
        return []

    length=1
    for num in digits:
        num=int(num)
        length*=len(dict.get(num))
    #print("length={}".format(length))
    answer=[""]*length
    th=length
    for n in range(len(digits)):
        num=int(digits[n])
        th/=len(dict.get(num))
        #print("th={}".format(th))
        pos=0
        #th=3ならaaabbbcccみたいに並べる
        for i in range(length):
            #print("pos={}".format(pos))
            answer[i]+=dict.get(num)[pos]
            #print("answer={}".format(answer))
            if (i+1)%th==0:
                pos+=1
            if pos==len(dict.get(num)):
                pos=0
    return answer
