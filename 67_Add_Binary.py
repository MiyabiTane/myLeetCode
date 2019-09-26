def binaryToDecimal(object):
    dec=0
    i=0
    while object!=0:
        mark=object%10
        dec+=mark*2**i
        object=(object-object%10)/10
        i+=1
    return dec

def decimalToBinary(object):
    bin_rev=[]
    while object!=0:
        bin_rev.append(object%2)
        object=(object-object%2)/2
        #print(bin_rev)
    bin_rev.reverse()
    num=0
    for i in range(len(bin_rev)):
        num+=bin_rev.pop()*10**i
    return num

def addBinary(a,b):
    sum_dec=binaryToDecimal(a)+binaryToDecimal(b)
    return decimalToBinary(sum_dec)
