def maxProfit(prices):
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


ans = maxProfit([7, 1, 5, 3, 6, 4])
print(ans)


