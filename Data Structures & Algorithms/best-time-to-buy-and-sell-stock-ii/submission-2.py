"""
Time complexity: O(N)
Space complexity: O(N)
Time: 8min
Approach: Monotonic stack
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stack = []
        for price in prices:
            if stack and stack[-1] >= price:
                max_profit += (stack[-1] - stack[0])
                stack = []
            stack.append(price)

        if stack:
            max_profit += (stack[-1] - stack[0])

        return max_profit