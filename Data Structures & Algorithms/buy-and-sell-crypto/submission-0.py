class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        window_start = 0
        for window_end in range(1, len(prices)):
            if prices[window_end] > prices[window_start]:
                max_profit = max(max_profit, prices[window_end] - prices[window_start])
            else:
                window_start = window_end

        return max_profit
