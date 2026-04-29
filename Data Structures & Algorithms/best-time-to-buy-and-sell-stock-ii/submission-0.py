class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        total_profit = 0
        for price in prices:
            if len(stack) == 0:
                stack.append(price)
            elif price > stack[-1]:
                if len(stack) > 1:
                    stack.pop()
                stack.append(price)
            else:
                if len(stack) == 2:
                    total_profit += (stack[-1] - stack[-2])
                    stack.pop()

                stack.pop()
                stack.append(price)

        if len(stack) == 2:
            total_profit += (stack[-1] - stack[-2])

        return total_profit    
