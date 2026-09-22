"""
Time complexity: O(N)
Space complexity: O(1)
Time: 5min
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev = None
        for num in prices:
            if prev is not None and num > prev:
                profit += num - prev
            prev = num
        
        return profit

        