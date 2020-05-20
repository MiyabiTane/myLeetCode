import numpy as np
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        print(weight)
        return weight


stock = StockSpanner()
stock.next(29)
stock.next(91)
stock.next(62)
stock.next(76)
stock.next(51)
