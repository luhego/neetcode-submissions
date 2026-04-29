class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_val = prices[0]
        max_val = prices[0]
        max_profit = 0
        for i in range(1, n):
            if prices[i] > max_val:
                max_val = prices[i]
                max_profit = max(max_profit, max_val - min_val)
            elif prices[i] < min_val:
                min_val = prices[i]
                max_val = prices[i]
        
        return max_profit