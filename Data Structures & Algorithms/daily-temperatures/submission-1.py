"""
Time complexity: O(N)
Space complexity: O(N)
Time: 11min
Topic: Stack, Monotonic Stack
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((temp, i))

        return result