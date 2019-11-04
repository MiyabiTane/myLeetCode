def intToRoman(num):
    #dict={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    if num==0:
        return ''
    elif num<=3:
        return "I"+intToRoman(num-1)
    elif num==4:
        return "IV"+intToRoman(num-4)
    elif 5<=num and num<9:
        return "V"+intToRoman(num-5)
    elif num==9:
        return "IX"+intToRoman(num-9)
    elif 10<=num and num<40:
        return "X"+intToRoman(num-10)
    elif 40<=num and num<50:
        return "XL"+intToRoman(num-40)
    elif 50<=num and num<90:
        return "L"+intToRoman(num-50)
    elif 90<=num and num<100:
        return "XC"+intToRoman(num-90)
    elif 100<=num and num<400:
        return "C"+intToRoman(num-100)
    elif 400<=num and num<500:
        return "CD"+intToRoman(num-400)
    elif 500<=num and num<900:
        return "D"+intToRoman(num-500)
    elif 900<=num and num<1000:
        return "CM"+intToRoman(num-900)
    else:
        return "M"+intToRoman(num-1000)
