"""
Time complexity: O(N)
Space complexity: O(1)
Time: 13min
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        left = 0
        for right in range(n):
            if right > left:
                max_profit = max(max_profit, prices[right] - prices[left])
            
            if prices[right] <= prices[left]:
                left = right
        
        return max_profit