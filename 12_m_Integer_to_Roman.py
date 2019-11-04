def intToRoman(num):
    dict={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    ans=""
    #dict doesn't have order
    keys=sorted(dict,reverse=True)
    for key in keys:
        #print(key)
        while key<=num:
            #print("get")
            ans+=dict.get(key)
            num-=key
    return ans
