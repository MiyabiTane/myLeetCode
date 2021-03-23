class Solution(object):
    def maxProfit(self, prices):
        min_ = prices[0]
        profit = 0
        for price in prices:
            if price < min_:
                min_ = price
            elif price - min_ > profit:
                profit = price - min_
        return profit


stock = [7, 1, 5, 3, 6, 4]
sol = Solution()
ans = sol.maxProfit(stock)
print(ans)


