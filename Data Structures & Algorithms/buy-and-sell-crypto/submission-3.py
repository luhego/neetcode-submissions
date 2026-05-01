"""
Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        n = len(prices)
        curr_smallest = prices[0]
        for i in range(1, n):
            if prices[i] >= curr_smallest:
                curr_profit = prices[i] - curr_smallest
                max_profit = max(max_profit, curr_profit)
            else:
                curr_smallest = prices[i]
        
        return max_profit
        