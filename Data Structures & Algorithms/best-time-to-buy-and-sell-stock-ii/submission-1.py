class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0

        max_profit = 0
        while i < n:
            start = i
            while i + 1 < n and prices[i] <= prices[i + 1]:
                i += 1

            if i > start:
                max_profit += (prices[i] - prices[start])

            i += 1

        return max_profit
