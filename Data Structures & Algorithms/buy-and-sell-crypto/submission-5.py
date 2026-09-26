"""
Time complexity: O(N)
Space complexity: O(1)
Time: 4min
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        n = len(prices)
        max_profit = 0
        for right in range(1, n):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
        
        return max_profit
