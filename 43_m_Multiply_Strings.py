def multiply(num1,num2):
    dict={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
    dict2={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",0:"0"}
    int1=0
    for i in range(len(num1)):
        int1+=dict.get(num1[i])*(10**(len(num1)-i-1))
    int2=0
    for i in range(len(num2)):
        int2+=dict.get(num2[i])*(10**(len(num2)-i-1))
    mul=int1*int2
    ans=""
    while True:
        num=mul%10
        #print(dict2.get(num))
        ans=dict2.get(num)+ans
        if mul<10:
            break
        mul=mul//10
    return ans

answer=multiply("123","456")
print(answer)