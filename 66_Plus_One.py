def plusOne(digits):
    num=0
    for i in range(len(digits)):
        num+=digits.pop()*10**i
        #print(num)
    num+=1
    while num!=0:
        digits.append(num%10)
        num=(num-num%10)/10
    digits.reverse()
    return digits
