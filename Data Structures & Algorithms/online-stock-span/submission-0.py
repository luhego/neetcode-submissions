class StockSpanner:

    def __init__(self):
        self.past_prices = []
        

    def next(self, price: int) -> int:
        i = len(self.past_prices) - 1
        span = 1
        while i >= 0 and self.past_prices[i] <= price:
            span += 1
            i -= 1
        self.past_prices.append(price)
        return span
      


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)