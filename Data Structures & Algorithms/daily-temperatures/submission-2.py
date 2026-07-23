"""
Time complexity: O(N)
Space complexity: O(N)
Time: 7min
Topic: Stack, Monotonic Stack
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_i = stack.pop()
                answer[prev_i] = i - prev_i
            stack.append((temp, i))
        
        return answer