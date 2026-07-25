"""
Time complexity: O(1)
Space complexity: O(1)
Time:
"""
class StockSpanner:

    def __init__(self):
        self.prices = []
        
    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1][0] <= price:
            _, prev_span = self.prices.pop()
            span += prev_span
        self.prices.append((price, span))
        return self.prices[-1][1]
      


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)