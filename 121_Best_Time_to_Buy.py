def maxProfit(prices):
    if len(prices)<2:
        return 0
    pro=0
    min=max(prices)
    for i in range(len(prices)):
        if prices[i]<min:
            min=prices[i]
        elif prices[i]-min>pro:
            pro=prices[i]-min
    return pro
