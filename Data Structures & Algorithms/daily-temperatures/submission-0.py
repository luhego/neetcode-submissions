class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = []
        for j, t in enumerate(temperatures):
            if len(stack) > 0 and stack[-1][0] < t:
                while len(stack) > 0 and t > stack[-1][0]:
                    old_t, i = stack.pop()
                    result[i] = j - i

            stack.append((t, j))

        return result
