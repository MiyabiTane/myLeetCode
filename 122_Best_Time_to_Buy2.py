def maxProfit(prices):
    if len(prices)<2:
        return 0
    pro=0
    for i in range(len(prices)-1):
        if prices[i+1]>prices[i]:
            pro+=prices[i+1]-prices[i]
    return pro

    """if len(prices)<2:
        return 0
    valley=prices[0]
    peak=0
    pro=0
    flag=0
    for i in range(len(prices)-1):
        if prices[i+1]<prices[i]:
            if flag==1:
                pro+=peak-valley
            valley=prices[i+1]
            flag=0
        elif prices[i+1]>prices[i]:
            peak=prices[i+1]
            flag=1
    if flag==1:
        pro+=peak-valley
    return pro"""
