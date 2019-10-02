#when there is vally and peak, we alwaly increase the profit
def maxProfit(prices):
    if len(prices)<2:
        return 0
    valley=0
    peak=0
    pro=0
    flag=0
    for i in range(1,len(prices)):
        if prices[i]<prices[i-1]:
            if flag==2:
                pro+=peak-valley
            valley=prices[i]
            flag=1
        elif flag==1 and prices[i]>prices[i-1]:
            peak=prices[i]
            flag=2
        #print(flag)
    if flag==0:
        pro=prices[-1]-prices[0]
    return pro
