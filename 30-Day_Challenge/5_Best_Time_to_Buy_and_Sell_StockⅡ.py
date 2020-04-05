def maxProfit(prices):
    profit = 0
    for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            profit+=(prices[i+1]-prices[i])
    return profit


ans = maxProfit([7, 6, 4, 3, 1])
print(ans)

"""
def maxProfit(prices):
    if len(prices)<2:
        return 0
    profit = 0
    pos = 0
    while pos<=len(prices)-1:
        while prices[pos] > prices[pos+1]:
            pos += 1
            if pos==len(prices)-1:
                return profit
        profit -= prices[pos]  # buy
        while prices[pos] <= prices[pos+1]:
            pos += 1
            if pos==len(prices)-1:
                return profit+prices[pos]
        profit += prices[pos]
    return profit
"""




