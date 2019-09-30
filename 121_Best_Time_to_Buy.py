def maxProfit(prices):
    pro=-1
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if pro<prices[j]-prices[i]:
                pro=prices[j]-prices[i]
    if pro<=0:
        return 0
    return pro
